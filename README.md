# 🛡️ PKI: Public Key Infrastructure Implementation

## 📖 Overview

The **PKI** project offers a foundational implementation of Public Key Infrastructure using Python. It enables secure document exchange through the generation and validation of X.509 certificates, leveraging asymmetric encryption techniques.

## 🚀 Features

- **Root and Leaf Certificate Authorities (CAs):** Establishes a hierarchical trust model with a Root CA and subordinate Leaf CAs. 🔒
- **Digital Signature Generation:** Securely signs documents to ensure authenticity and integrity. ✍️
- **Document Encryption:** Encrypts documents for confidential transmission. 🔐
- **Certificate Validation:** Verifies the authenticity and validity of certificates. ✅
- **Revocation Mechanism:** Manages and checks certificate revocation status. 🚫

## 🛠️ Technologies Used

- **Programming Language:** Python 🐍
- **Cryptographic Library:** OpenSSL 🔑
- **Certificate Format:** X.509 📜

## 📁 Project Structure

```plaintext
├── rootCA.crt          # Root Certificate Authority Certificate
├── rootCA.key          # Root Certificate Authority Private Key
├── leafCA.crt          # Leaf Certificate Authority Certificate
├── leafCA.key          # Leaf Certificate Authority Private Key
├── sender.py           # Sender's script to encrypt and sign documents
├── receiver.py         # Receiver's script to decrypt and verify documents
├── certificate.py      # Module to handle certificate operations
└── document.xml        # Sample XML document for encryption
```

## 📥 Installation

### Prerequisites

- Python 3.6 or higher 🐍
- OpenSSL installed on your system 🔧

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/muhai21/pki.git
   cd pki
   ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

## Install required dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## ⚙️ Usage

### Generating Certificates

- Create Root CA:

  ```bash
  Copy
  python certificate.py --create-root-ca
  ```

- Create Leaf CA:

  ```bash
  Copy
  python certificate.py --create-leaf-ca
  ```

### Signing and Encrypting Documents

- Sender:

  ```bash
  Copy
  python sender.py --encrypt --sign --input document.xml --output encrypted_document.xml
  ```

- Receiver:

  ```bash
  Copy
  python receiver.py --decrypt --verify --input encrypted_document.xml --output decrypted_document.xml
  ```

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details. ⚖️

## 🤝 Contributing

Contributions are welcome! Please see the CONTRIBUTING.md file for guidelines on how to contribute to this project. 🙌

## 📚 References

- [Public Key Infrastructure (PKI)](https://en.wikipedia.org/wiki/Public_key_infrastructure) 📖
- [X.509 Certificate Standard](https://en.wikipedia.org/wiki/X.509) 📜
