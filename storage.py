import json
import os

FILENAME = "passwords.json"

def save_password(name, encrypted_password):
    data = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            data = json.load(file)
    data[name] = encrypted_password.decode()
    with open(FILENAME, "w") as file:
        json.dump(data, file)

def load_password(name):
    if not os.path.exists(FILENAME):
        return None
    with open(FILENAME, "r") as file:
        data = json.load(file)
        if name in data:
            return data[name].encode()
    return None
