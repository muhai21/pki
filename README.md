🛡️PKI: Public Key Infrastructure Implementation

Overview

The PKI project provides a foundational implementation of Public Key Infrastructure using Python. It facilitates secure document exchange through the generation and validation of X.509 certificates, leveraging asymmetric encryption techniques.

🚀 Features





Root and Leaf Certificate Authorities (CAs): Establish a hierarchical trust model with a Root CA and subordinate Leaf CAs.



Digital Signature Generation: Securely sign documents to ensure authenticity and integrity.



Document Encryption: Encrypt documents for confidential transmission.



Certificate Validation: Verify the authenticity and validity of certificates.



Revocation Mechanism: Manage and check certificate revocation status.

🔧 Technologies Used





Programming Language: Python



Cryptographic Library: OpenSSL



Certificate Format: X.509

📁 Project Structure

├── rootCA.crt          # Root Certificate Authority Certificate
├── rootCA.key          # Root Certificate Authority Private Key
├── leafCA.crt          # Leaf Certificate Authority Certificate
├── leafCA.key          # Leaf Certificate Authority Private Key
├── sender.py           # Sender's script to encrypt and sign documents
├── receiver.py         # Receiver's script to decrypt and verify documents
├── certificate.py      # Module to handle certificate operations
└── document.xml        # Sample XML document for encryption

📥 Installation

Prerequisites





Python 3.6+



OpenSSL installed on your system

Setup





Clone the repository:

git clone https://github.com/muhai21/pki.git
cd pki



(Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`



Install required dependencies:

pip install -r requirements.txt

🛠️ Usage

Generating Certificates





Create Root CA:

python certificate.py --create-root-ca



Create Leaf CA:

python certificate.py --create-leaf-ca

Signing and Encrypting Documents





Sender:

python sender.py --encrypt --sign --input document.xml --output encrypted_document.xml



Receiver:

python receiver.py --decrypt --verify --input encrypted_document.xml --output decrypted_document.xml

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🤝 Contributing

Contributions are welcome! Please refer to the CONTRIBUTING.md for guidelines on how to contribute to this project.

📚 References





Public Key Infrastructure (PKI) - Wikipedia



X.509 Certificate Standard
