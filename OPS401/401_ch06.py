#!/usr/bin/python3

# Script Name:                  Challenge 06
# Author:                       Mack Dirks
# Date of latest revision:      07/18/2023
# Purpose:                      File Encryption Script Part 1 of 3

# Imports cryptographic library
from cryptography.fernet import Fernet
from os.path import exists

# Variable declaration
answer = "yes"

# Function to generate the key
def gen_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as k_file:
        k_file.write(key)

# Function to load our key:
def key_load():
    return open("key.key", "rb").read()


# File encryption function
def file_encryption():
    f = Fernet(key)
    file_location = input("\nEnter the file path: ")
    with open(file_location, "rb") as file:
        data = file.read()
    encrypt_file = f.encrypt(data)
    with open(file_location, "wb") as file:
        file.write(encrypt_file)

# File decryption function
def file_decryption():
    f = Fernet(key)
    file_location = input("\nEnter the file path: ")
    with open(file_location, "rb") as file:
        data = file.read()
        decrypt_file = f.decrypt(data)
    with open(file_location, "wb") as file:
        file.write(decrypt_file)

# Message encryption function
def message_encryption():
    message = input("\nEnter a message to encrypt: ")
    encrypt_message = message.encode()
    f = Fernet(key)
    encrypt_version = f.encrypt(encrypt_message)
    print("\nHere is the encrypted message: ")
    print(encrypt_version)

# Message decryption function
def message_decryption():
    message = input("\nEnter a message to decrypt: ")
    decrypt_message = str.encode(message)
    f = Fernet(key)
    decrypt_version = f.decrypt(decrypt_message)
    print("\nHere is the encrypted message: ")
    print(decrypt_version)

# Menu function
def menu():
    print("\nHere are your 4 options: ")
    print("\nTo Encrypt a File, select 1")
    print("To Decrypt a File, select 2")
    print("To Encrypt a Message, select 3")
    print("To Decrypt a Message, select 4")
    user_choice = input("\nSelect your option: ")

    if (user_choice == "1"):
        file_encryption()
        print("\nThe file was encrypted")
    elif (user_choice == "2"):
        file_decryption()
        print("\nThe message was decrypted")
    elif (user_choice == "3"):
        message_encryption()
    elif(user_choice == "4"):
        message_decryption()
    else:
        print("Inappropriate selection!")

# Main

key_exists = exists("./key.key")

if key_exists:
    key = key_load()
else:
    gen_key()
    key = key_load()

while True:
    menu()
    answer = input("\nDo you want to try again? yes or no: ")
    if answer == "no":
        print("\nEnjoy your day!")
        break