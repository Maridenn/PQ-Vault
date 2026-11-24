<div align="center">

<img src="https://t4.ftcdn.net/jpg/07/19/26/97/360_F_719269705_L0sglwWqLgB5qs8zM0X4geXGCimf57el.jpg" width="480" alt="PQ-Vault Banner"/>

# PQ-Vault
### Hybrid post-quantum file encryption

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/Cryptography-AES--256--GCM-2563EB?style=flat-square)
![PQC](https://img.shields.io/badge/Post--Quantum-ML--KEM--768-7C3AED?style=flat-square)
![Standard](https://img.shields.io/badge/NIST-FIPS%20203-0F766E?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Development-E5A000?style=flat-square)

</div>

---

## Project Overview

The advancement of quantum computing introduces new challenges to modern cryptography. Public-key algorithms such as RSA and Elliptic Curve Cryptography (ECC) are vulnerable to sufficiently capable quantum computers.

One emerging concern is known as **Harvest Now, Decrypt Later (HNDL)**, where attackers collect encrypted information today with the intention of decrypting it when quantum technology becomes powerful enough.

**PQ-Vault** is a python based command line application designed to explore this threat through hybrid post-quantum file encryption.

It combines:

- **ML-KEM-768 (FIPS 203):** A NIST-standardized post-quantum key encapsulation mechanism.
- **AES-256-GCM:** An authenticated symmetric encryption algorithm for protecting file contents.
- **HKDF-SHA256:** A key derivation function used to derive an AES encryption key from the ML-KEM shared secret.

The objective is to create a simple file vault that allows users to generate cryptographic keys, encrypt files, and recover their original contents securely.

## Cryptographic Architecture

PQ-Vault separates key establishment from file encryption. Each algorithm has a specific responsibility.

| Component | Algorithm | Responsibility |
|---|---|---|
| Key Encapsulation | ML-KEM-768 | Establishes a shared secret |
| Key Derivation | HKDF-SHA256 | Derives a 256-bit encryption key |
| File Encryption | AES-256-GCM | Encrypts and authenticates file contents |
| Output Format | `.pq` | Stores the encrypted file and required metadata |

### Encryption Process

1. The recipient generates an ML-KEM-768 public/private key pair.
2. The sender uses the recipient's public key to encapsulate a shared secret.
3. ML-KEM produces a shared secret and an encapsulation ciphertext.
4. HKDF-SHA256 derives a 256-bit AES encryption key from the shared secret.
5. AES-256-GCM encrypts the original file.
6. The application combines the ML-KEM ciphertext, nonce, and authenticated encrypted payload into a `.pq` file.

### Decryption Process

1. The recipient opens the `.pq` encrypted file.
2. The application extracts the ML-KEM ciphertext and AES-GCM nonce.
3. The recipient's private key decapsulates the ML-KEM ciphertext to recover the shared secret.
4. HKDF-SHA256 derives the same AES encryption key.
5. AES-256-GCM verifies the authentication tag and decrypts the file.
6. The original file is recovered if authentication succeeds.

## Encrypted File Format

PQ-Vault uses a custom `.pq` file format to combine the information required for decryption.

The proposed initial format is:

```text
+----------------------------------+
| Magic Bytes / Format Version     |
+----------------------------------+
| ML-KEM-768 Ciphertext (1088 B)   |
+----------------------------------+
| AES-GCM Nonce (12 B)             |
+----------------------------------+
| AES-GCM Encrypted Payload        |
| (Ciphertext + Authentication Tag)|
+----------------------------------+
```

The AES-GCM authentication tag is included in the encrypted payload produced by the cryptography library.

This structure allows the application to store the encapsulation ciphertext alongside the encrypted file without storing the secret AES key.

## Project Features

### Planned Core Features

| Feature | Description | Status |
|---|---|---|
| Key Generation | Generate ML-KEM-768 public/private keys | Planned |
| File Encryption | Encrypt files using AES-256-GCM | Planned |
| File Decryption | Recover encrypted files using the private key | Planned |
| Hybrid Key Establishment | Combine ML-KEM with HKDF and AES | Planned |
| `.pq` File Format | Store encryption metadata and payload | Planned |
| Error Handling | Handle invalid keys and corrupted files | Planned |
| Security Testing | Test tampering and incorrect-key scenarios | Planned |

*Feature status will be updated as development progresses.*

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12+ | Main programming language |
| cryptography | AES-256-GCM and HKDF-SHA256 |
| ML-KEM implementation | Post-quantum key encapsulation |
| Git | Version control |
| GitHub | Source code hosting and project documentation |


## Project Structure

The planned repository structure is:

```text
PQ-Vault/
│
├── main.py                 # Command-line interface
├── crypto_utils.py         # Cryptographic operations
│
├── keys/                   # Generated key files
│
├── encrypted/              # Encrypted .pq files
│
├── tests/                  # Testing and validation
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Excluded files
│
└── docs/                   # Architecture and documentation
```


## Installation

### Prerequisites

- Python 3.12 or newer
- Git
- pip (Python package manager)

### 1. Clone the repository

```bash
git clone https://github.com/Maridenn/PQ-Vault.git

cd PQ-Vault
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv

.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

PQ-Vault is designed to provide three primary operations through a command-line interface.

```text
=============================================
             WELCOME TO PQ-VAULT
       Hybrid Post-Quantum File Vault
=============================================

1. Generate Cryptographic Keys
2. Encrypt a File
3. Decrypt a File
4. Exit

Enter your choice:
```

**Planned operations:**

| Command | Purpose |
|---|---|
| `keygen` | Generate the ML-KEM-768 key pair |
| `encrypt` | Encrypt a file into `.pq` format |
| `decrypt` | Decrypt a `.pq` file |

## Limitations

PQ-Vault is an educational cryptography project and a prototype, not a production ready file security product.

Its initial scope focuses on local file encryption and decryption.

Potential limitations include:

- Security depends on the correctness and maturity of the selected cryptographic libraries.
- Python does not provide guaranteed secure memory erasure for secret data.
- Private key protection depends on appropriate local storage and access controls.
- The initial implementation does not provide multi-user key management or network-based key exchange.
- The application does not replace established secure storage systems or operating-system security mechanisms.

## Future Improvements

Possible extensions beyond the initial project scope include:

- Multi-user encryption with different recipient public keys.
- Performance benchmarking against traditional RSA-based key establishment.
- Integration with network-based file transfer.
- Improved key storage and password-protected private keys.
- A graphical user interface.
- Additional post-quantum cryptographic experimentation.

## 13 — References

1. NIST. (2024). *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM).*  
   https://csrc.nist.gov/pubs/fips/203/final

2. NIST. (2024). *FIPS 197: Advanced Encryption Standard (AES).*  
   https://csrc.nist.gov/pubs/fips/197/final

3. NIST. (2010). *SP 800-56C Rev. 2: Recommendation for Key-Derivation Methods in Key-Establishment Schemes.*  
   https://csrc.nist.gov/pubs/sp/800/56/c/r2/final

4. Python Cryptographic Authority. *Cryptography Documentation.*  
   https://cryptography.io/