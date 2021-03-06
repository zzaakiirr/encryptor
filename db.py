import os
from sqlite3 import connect

DB_NAME = "database.db"


# TODO: Create class

def _create_db_if_needed():
    if os.path.isfile(DB_NAME):
        return

    conn = connect(DB_NAME)

    c = conn.cursor()
    c.execute('CREATE TABLE users (username text unique, password text)')
    c.execute('CREATE TABLE files (name text unique, password text)')

    conn.commit()
    conn.close()


def authenticate(username, password):
    _create_db_if_needed()

    conn = connect(DB_NAME)

    c = conn.cursor()
    c.execute('''SELECT * FROM users
                 WHERE username == :password and password == :password''',
              {"username": username, "password": password})

    result = c.fetchone() is not None
    conn.close()
    return result


def add_user(username, password):
    conn = connect(DB_NAME)

    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))

    conn.commit()
    conn.close()


def update_user_password(username, new_password):
    conn = connect(DB_NAME)

    c = conn.cursor()
    c.execute("UPDATE users SET password = ? WHERE username = ?",
              (new_password, username))

    conn.commit()
    conn.close()
