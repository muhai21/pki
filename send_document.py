#!/usr/bin/env python
# filepath: d:\pki\send_document.py
from sender import SEGSender
import requests

class ModifiedSEGSender(SEGSender):
    def send_document(self, xml_file_path, receiver_url):
        """Send signed XML document to receiver with mTLS, but disable hostname verification"""
        with open(xml_file_path, "rb") as f:
            xml_content = f.read()
        
        signed_xml = self.sign_xml(xml_content)
        
        try:
            response = requests.post(
                receiver_url,
                data=signed_xml,
                headers={"Content-Type": "application/xml"},
                cert=("segSender.crt", "segSender.key"),
                verify=False  # Disable SSL verification for testing
            )
            response.raise_for_status()
            print(f"Document successfully sent to {receiver_url}")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Failed to send document: {str(e)}")
            return False

if __name__ == "__main__":
    # Create sender instance with certificates
    sender = ModifiedSEGSender(
        private_key_path="segSender.key",
        certificate_path="segSender.crt", 
        ca_cert_path="rootCA.crt"
    )
    
    # Send the document
    result = sender.send_document(
        xml_file_path="document.xml",
        receiver_url="https://localhost:8443/receive"
    )
    
    if result:
        print("Document sending completed successfully")
    else:
        print("Document sending failed")
