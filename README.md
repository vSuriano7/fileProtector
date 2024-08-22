# FileProtector

## Overview

**FileProtector** is a simple Python script designed as an exercise to demonstrate basic file encryption and decryption using the AES (Advanced Encryption Standard) algorithm. The script allows users to securely encrypt and decrypt files using a password-based key derivation method.

## Features

- **Encrypt Files**: Convert plain text files into encrypted files with a `.enc` extension.
- **Decrypt Files**: Convert encrypted files back to their original form by removing the `.enc` extension.
- **Password-Based Encryption**: Uses a password to derive the AES key for encryption and decryption, ensuring that only users with the correct password can access the file contents.

## How to Use

1. **Encrypt a File**:
   - Run the script and choose option `1` to encrypt a file.
   - Provide the file path and a password.
   - The script will generate an encrypted file with the same name and an `.enc` extension.

2. **Decrypt a File**:
   - Run the script and choose option `2` to decrypt a file.
   - Provide the file path of the encrypted file (must end with `.enc`) and the correct password.
   - The script will generate the original file, removing the `.enc` extension.

## Prerequisites

- Python 3.x
- The `cryptography` library. Install it using pip:
  ```bash
  pip install cryptography
  ```

## Example

To encrypt a file named `document.txt`:

```bash
python file_protector.py
# Input: 1 (to encrypt)
# Input: document.txt
# Input: your_password
```

To decrypt `document.txt.enc`:

```bash
python file_protector.py
# Input: 2 (to decrypt)
# Input: document.txt.enc
# Input: your_password
```

## Notes

- This script is meant for educational purposes and as a demonstration of file encryption and decryption techniques.
- For production use, consider additional security practices and libraries.

# FileProtector

## Panoramica

**FileProtector** è un semplice script Python progettato come esercizio per dimostrare la cifratura e decifratura di file utilizzando l'algoritmo AES (Advanced Encryption Standard). Lo script consente agli utenti di cifrare e decifrare file in modo sicuro utilizzando un metodo di derivazione della chiave basato su password.

## Caratteristiche

- **Cifrare i File**: Convertire i file di testo normale in file cifrati con un'estensione `.enc`.
- **Decifrare i File**: Convertire i file cifrati nel loro formato originale rimuovendo l'estensione `.enc`.
- **Cifratura Basata su Password**: Utilizza una password per derivare la chiave AES per la cifratura e decifratura, assicurando che solo gli utenti con la password corretta possano accedere al contenuto dei file.

## Come Usare

1. **Cifrare un File**:
   - Esegui lo script e scegli l'opzione `1` per cifrare un file.
   - Fornisci il percorso del file e una password.
   - Lo script genererà un file cifrato con lo stesso nome e un'estensione `.enc`.

2. **Decifrare un File**:
   - Esegui lo script e scegli l'opzione `2` per decifrare un file.
   - Fornisci il percorso del file cifrato (deve terminare con `.enc`) e la password corretta.
   - Lo script genererà il file originale, rimuovendo l'estensione `.enc`.

## Requisiti

- Python 3.x
- La libreria `cryptography`. Installala utilizzando pip:
  ```bash
  pip install cryptography
  ```

## Esempio

Per cifrare un file chiamato `document.txt`:

```bash
python file_protector.py
# Inserisci: 1 (per cifrare)
# Inserisci: document.txt
# Inserisci: tua_password
```

Per decifrare `document.txt.enc`:

```bash
python file_protector.py
# Inserisci: 2 (per decifrare)
# Inserisci: document.txt.enc
# Inserisci: tua_password
```

## Note

- Questo script è pensato per scopi educativi e come dimostrazione delle tecniche di cifratura e decifratura dei file.
- Per un uso in produzione, considera pratiche di sicurezza aggiuntive e librerie specializzate.
