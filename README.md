# Encryptor
This program is used for encrypting and decrypting files.
When you encrypt file original file will be deleted. Vice versa with decryption. 

### Installation

Requires [Python](https://python.org/) tested on v3.6.9.

For correct working you have to install all modules from ```requirements.txt``` file:

```sh
$ python install -r requirements.txt
```
# Usage

For doing anything with this program, you should now default credentials:
+ username: `me`, password: `me`

If you are getting following error, then set `file=""`:
```sh
main.py: error: the following arguments are required: file
```


##### Takes next arguments (crypto):
- `file`: File name to encrypt
- `--encrypt`: Flag indicating encryption need
- `--decrypt`: Flag indicating decryption need

##### User authentication:
- `--addUser`: Adding new user
- `--updatePassword`: Updating user password

##### Examples
```sh
python main.py test15.txt --encrypt
python main.py test15.txt --decrypt
```
```sh
python main.py --addUser file=""
```

# Authors
+ Zakir Dzhamaliddinov - pfrbhxbr@gmail.com

