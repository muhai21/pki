import requests
from lxml import etree
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from datetime import datetime
import os

class SEGSender:
    def __init__(self, private_key_path, certificate_path, ca_cert_path):
        self.private_key = self._load_private_key(private_key_path)
        self.certificate = self._load_certificate(certificate_path)
        self.ca_cert = self._load_certificate(ca_cert_path)
        
    def _load_private_key(self, path):
        with open(path, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    
    def _load_certificate(self, path):
        with open(path, "rb") as cert_file:
            return cert_file.read()
    
    def sign_xml(self, xml_str):
        """Sign the XML document using the sender's private key"""
        root = etree.fromstring(xml_str)
        
        # Add timestamp if not present
        timestamp = root.find(".//TimestampForSignature")
        if timestamp is None:
            timestamp = etree.SubElement(root, "TimestampForSignature")
        timestamp.text = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Serialize to canonical XML (for consistent signing)
        xml_to_sign = etree.tostring(root, method="c14n")
        
        # Sign the document
        signature = self.private_key.sign(
            xml_to_sign,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        
        # Add signature to XML
        signature_element = etree.SubElement(root, "Signature")
        signature_element.text = signature.hex()
        
        return etree.tostring(root, pretty_print=True)
    
    def send_document(self, xml_file_path, receiver_url):
        """Send signed XML document to receiver with mTLS"""
        with open(xml_file_path, "rb") as f:
            xml_content = f.read()
        
        signed_xml = self.sign_xml(xml_content)
        
        try:
            response = requests.post(
                receiver_url,
                data=signed_xml,
                headers={"Content-Type": "application/xml"},
                cert=("segSender.crt", "segSender.key"),
                verify="rootCA.crt"
            )
            response.raise_for_status()
            print(f"Document successfully sent to {receiver_url}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to send document: {str(e)}")
            return False