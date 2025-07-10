import os
from cryptography.fernet import Fernet

# Generate and save a key (should be done only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_path, "wb") as file:
        file.write(encrypted)

# Decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(file_path, "wb") as file:
        file.write(decrypted)

# Encrypt all files in a given directory
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            encrypt_file(full_path, key)
            print(f"[+] Encrypted: {full_path}")

# Decrypt all files in a given directory
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            decrypt_file(full_path, key)
            print(f"[+] Decrypted: {full_path}")

# === Usage ===
# Run only once to generate the key
# generate_key()

# Load key
key = load_key()

# Encrypt or decrypt the folder
folder = "Screenshot 2023-05-01 183632.ping"  # Replace with your folder path

# To encrypt files:
encrypt_folder(folder, key)

# To decrypt files:
# decrypt_folder(folder, key)
