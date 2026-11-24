def display_banner():
    print("\n" + "=" * 45)
    print("WELCOME TO PQ-VAULT")
    print("Hybrid Post-Quantum File Vault")
    print("=" * 45)


def display_menu():
    print("\nPlease select an operation:")
    print("-" * 45)
    print("1. Generate Cryptographic Keys")
    print("2. Encrypt a File")
    print("3. Decrypt a File")
    print("4. Exit")
    print("-" * 45)


def generate_keys():
    print("\nKey generation is not implemented yet.")


def encrypt_file():
    print("\nFile encryption is not implemented yet.")


def decrypt_file():
    print("\nFile decryption is not implemented yet.")


def main():
    display_banner()

    while True:
        display_menu()

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            generate_keys()

        elif choice == "2":
            encrypt_file()

        elif choice == "3":
            decrypt_file()

        elif choice == "4":
            print("\nThank you for using PQ-Vault!")
            print("Exiting application...")
            break

        else:
            print("\n[ERROR] Invalid choice.")
            print("Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()