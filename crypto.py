from cryptography.fernet import Fernet

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        return key

key = load_key()
fernet = Fernet(key)

def encrypt_password(password: str) -> bytes:
    return fernet.encrypt(password.encode())

def decrypt_password(token: bytes) -> str:
    return fernet.decrypt(token).decode()
