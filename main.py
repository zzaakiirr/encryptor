import argparse
import getpass

from db import authenticate
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

    parser.add_argument('-u', '--username',
                        default=None,
                        help="Username for new user")

    parser.add_argument('-p', '--password',
                        default=None,
                        help="Password for new user")

    parser.add_argument('--addUser', help='Add new user')
    parser.add_argument('--updatePassword', help='Update user password')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    print(args)

    # Parser args
    should_encrypt = args.encrypt
    should_decrypt = args.decrypt
    filename = args.file

    # add_user = args.addUser
    # updatePassword = args.updatePassword
    # username = args.username
    # password = args.password

    if should_encrypt and should_decrypt:
        error = "You cannot encrypt and decrypt at the same time. Choose one"
        raise Exception(error)

    # if ()

    username = getpass.getpass("Username: ")
    password = getpass.getpass("Password: ")

    is_authorized = authenticate(username, password)
    if not is_authorized:
        raise Exception("Credentials are invalid")

    if args.encrypt:
        encrypt_file(filename)

    if args.decrypt:
        decrypt_file(filename)
