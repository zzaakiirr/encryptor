from sqlite3 import connect, IntegrityError
import os

import pyAesCrypt

from db import DB_NAME
from helpers import create_random_string


# encryption/decryption buffer size - 64K
BUFFER_SIZE = 64 * 1024


def encrypt_file(filename):
    password = create_random_string()

    conn = connect(DB_NAME)

    c = conn.cursor()
    try:
        c.execute("INSERT INTO files VALUES (?, ?)", (filename, password))
    except IntegrityError:
        raise Exception("File with this name was already encoded. " +
            "Please use another name")

    conn.commit()
    conn.close()

    try:
        file_out = f"{filename}.aes"
        pyAesCrypt.encryptFile(filename, file_out, password, BUFFER_SIZE)
    except Exception as e:
        print(e)
    else:
        os.remove(filename)


def decrypt_file(filename):
    conn = connect(DB_NAME)

    c = conn.cursor()
    c.execute("SELECT password FROM files WHERE name == :filename",
              {"filename": filename})

    fetch = c.fetchone()
    if fetch is None:
        raise Exception("No such file in db")
    else:
        password = fetch[0]

    conn.close()

    try:
        file_in = f"{filename}.aes"
        pyAesCrypt.decryptFile(file_in, filename, password, BUFFER_SIZE)
    except Exception as e:
        print(e)
    else:
        os.remove(file_in)
