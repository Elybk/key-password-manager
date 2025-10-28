from crypto import encrypt_password, decrypt_password
from storage import save_password, load_password

def main():
    print("🔐 Simple Key Password Manager")
    print("1. Save a new password")
    print("2. Retrieve a password")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        name = input("Enter account name: ")
        password = input("Enter password: ")
        encrypted = encrypt_password(password)
        save_password(name, encrypted)
        print("✅ Password saved securely.")
    elif choice == "2":
        name = input("Enter account name: ")
        encrypted = load_password(name)
        if encrypted:
            decrypted = decrypt_password(encrypted)
            print(f"🔑 Password for {name}: {decrypted}")
        else:
            print("❌ No password found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
