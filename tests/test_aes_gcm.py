
from cryptography.exceptions import InvalidTag

from crypto_utils import (
    generate_test_key,
    encrypt_data,
    decrypt_data
)


def main():
    print("Testing PQ-Vault AES-256-GCM")
    print("--------------------------------")

    # Generate a temporary secret key
    key = generate_test_key()
    print("[SUCCESS] AES-256 key generated.")

    # Create a test message
    original_message = b"Hello! This is a PQ-Vault encryption test."

    # Encrypt the message
    nonce, encrypted_message = encrypt_data(
        original_message,
        key
    )

    print("[SUCCESS] Message encrypted.")
    print("Encrypted data:", encrypted_message.hex())

    # Decrypt the message
    decrypted_message = decrypt_data(
        nonce,
        encrypted_message,
        key
    )

    print("[SUCCESS] Message decrypted.")

    # verify that the original message is restored
    assert decrypted_message == original_message

    print("[SUCCESS] Original message successfully restored.")

    # test whether modified ciphertext is detected
    tampered_message = bytearray(encrypted_message)
    tampered_message[0] ^= 1

    try:
        decrypt_data(nonce, bytes(tampered_message), key)
        raise AssertionError("Modified data was not detected.")

    except InvalidTag:
        print("[SUCCESS] Modified data was detected!")

    print("--------------------------------")
    print("All AES-256-GCM tests passed!")


if __name__ == "__main__":
    main()