import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

AES_KEY_SIZE = 32

NONCE_SIZE = 12


def generate_test_key():
    """
    Generate a temporary AES-256 key for testing.

    In the final PQ-Vault design, this key will instead
    be derived from the ML-KEM shared secret using HKDF.
    """
    return AESGCM.generate_key(bit_length=256)


def encrypt_data(plaintext: bytes, key: bytes):
    """
    Encrypt data using AES-256-GCM.

    Returns:
        nonce: The nonce used during encryption.
        ciphertext: Encrypted data with its authentication tag.
    """

    if len(key) != AES_KEY_SIZE:
        raise ValueError("AES-256 requires a 32-byte key.")

    # generate a fresh random nonce
    nonce = os.urandom(NONCE_SIZE)

    # create an AES-GCM encryption object
    aesgcm = AESGCM(key)

    # encrypt the original data
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    return nonce, ciphertext


def decrypt_data(nonce: bytes, ciphertext: bytes, key: bytes):
    """
    Decrypt AES-256-GCM encrypted data.

    Returns:
        The original plaintext.
    """

    if len(key) != AES_KEY_SIZE:
        raise ValueError("AES-256 requires a 32-byte key.")

    if len(nonce) != NONCE_SIZE:
        raise ValueError("AES-GCM requires a 12-byte nonce.")

    # create an AES-GCM decryption object
    aesgcm = AESGCM(key)

    # decrypt and verify the authentication tag
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    return plaintext