import argparse
import getpass

import db
from crypto import encrypt_file, decrypt_file


def get_args():
    parser = argparse.ArgumentParser()

    # MARK: - Encrypt / Decrypt

    parser.add_argument('file', help='File to encrypt')

    parser.add_argument('--encrypt',
                        action="store_true",
                        default=None,
                        help='Flag if needed to encrypt')

    parser.add_argument('--decrypt',
                        default=None,
                        action="store_true",
                        help='Flag if needed to decrypt')


    # MARK: - User authentication

    parser.add_argument('--addUser',
                        default=None,
                        action="store_true",
                        help='Add new user')

    parser.add_argument('--updatePassword',
                        default=None,
                        action="store_true",
                        help='Update user password')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    print(args)

    # Parser args
    should_encrypt = args.encrypt
    should_decrypt = args.decrypt
    filename = args.file

    add_user = args.addUser
    update_password = args.updatePassword

    if should_encrypt and should_decrypt:
        msg = "You can't encrypt and decrypt at the same time. Choose one"
        raise Exception(msg)

    if add_user and update_password:
        msg = "You can't add user and change user password at the same time." + \
              "Choose one"
        raise Exception(msg)

    username = getpass.getpass("Username: ")
    password = getpass.getpass("Password: ")

    is_authorized = db.authenticate(username, password)
    if not is_authorized:
        raise Exception("Credentials are invalid")

    if args.encrypt:
        encrypt_file(filename)

    elif args.decrypt:
        decrypt_file(filename)

    elif add_user:
        print("ATTENTION: Adding new user")
        username = getpass.getpass("Username: ")
        password = getpass.getpass("Password: ")

        db.add_user(username, password)

    elif update_password:
        print("ATTENTION: Updating user password")
        username = getpass.getpass("Username: ")
        new_password = getpass.getpass("New password: ")

        db.update_user_password(username, password)
