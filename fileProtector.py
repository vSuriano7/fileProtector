from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Funzione per generare una chiave AES dalla password
def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

# Funzione per cifrare un file
def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)
    
    with open(file_path, 'rb') as f:
        data = f.read()

    # Padding dei dati
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Cifratura
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Salva i dati cifrati in un nuovo file
    with open(file_path + '.enc', 'wb') as f:
        f.write(salt + iv + encrypted_data)

    print(f"File cifrato e salvato come {file_path + '.enc'}")

# Funzione per decifrare un file
def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = generate_key(password, salt)

    # Decifratura
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Rimozione del padding
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # Salva i dati decifrati con il nome originale
    original_file_path = file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as f:
        f.write(unpadded_data)

    print(f"File decifrato e salvato come {original_file_path}")

# Funzione principale
def main():
    action = input("Digita 1 per cifrare o 2 per decifrare un file: ").strip()
    file_path = input("Inserisci il percorso del file: ").strip()
    password = input("Inserisci la password: ").strip()

    if action == '1':
        encrypt_file(file_path, password)
    elif action == '2':
        if file_path.endswith('.enc'):
            decrypt_file(file_path, password)
        else:
            print("Errore: il file da decifrare deve avere l'estensione '.enc'.")
    else:
        print("Azione non riconosciuta. Riprova.")

if __name__ == "__main__":
    main()
