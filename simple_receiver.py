from flask import Flask, request, jsonify
from lxml import etree
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)

class SEGReceiver:
    def __init__(self, private_key_path, certificate_path, ca_cert_path, sender_cert_path):
        self.private_key = self._load_private_key(private_key_path)
        self.certificate = self._load_certificate(certificate_path)
        self.ca_cert = self._load_certificate(ca_cert_path)
        self.sender_cert = self._load_certificate(sender_cert_path)
        self.sender_pub_key = self.sender_cert.public_key()
        
    def _load_private_key(self, path):
        with open(path, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    
    def _load_certificate(self, path):
        with open(path, "rb") as cert_file:
            return x509.load_pem_x509_certificate(
                cert_file.read(),
                default_backend()
            )
    
    def verify_signature(self, xml_str):
        """Verify the XML signature using the sender's public key"""
        try:
            root = etree.fromstring(xml_str)
            
            # Extract signature
            signature_element = root.find(".//Signature")
            if signature_element is None:
                raise ValueError("No signature found in XML")
                
            signature = bytes.fromhex(signature_element.text)
            root.remove(signature_element)  # Remove signature before verification
            
            # Serialize to canonical XML (must match signed version)
            xml_to_verify = etree.tostring(root, method="c14n")
            
            # Verify signature
            self.sender_pub_key.verify(
                signature,
                xml_to_verify,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            
            return True, etree.tostring(root, pretty_print=True)
        except Exception as e:
            return False, f"Signature verification failed: {str(e)}"

@app.route('/receive', methods=['POST'])
def receive_document():
    try:
        # Process the XML document
        xml_data = request.data
        is_valid, result = receiver.verify_signature(xml_data)
        
        if is_valid:
            print("Successfully received and verified document:")
            print(result.decode())
            return jsonify({
                "status": "success",
                "document": result.decode()
            }), 200
        else:
            print(f"Document verification failed: {result}")
            return jsonify({
                "status": "error",
                "message": result
            }), 400
            
    except Exception as e:
        print(f"Error processing document: {str(e)}")
        return jsonify({
            "status": "error",
            "message": f"Processing error: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Initialize receiver with certificates
    receiver = SEGReceiver(
        private_key_path="segReceiver.key",
        certificate_path="segReceiver.crt",
        ca_cert_path="rootCA.crt",
        sender_cert_path="segSender.crt"
    )
    
    # Configure Flask with SSL
    context = ('segReceiver.crt', 'segReceiver.key')
    
    app.run(
        host='0.0.0.0',
        port=8443,
        ssl_context=context
    )
