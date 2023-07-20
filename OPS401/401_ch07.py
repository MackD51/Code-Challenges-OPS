#!/usr/bin/python3

# Script Name:                  Challenge 07
# Author:                       Mack Dirks
# Date of latest revision:      07/18/2023
# Purpose:                      File Encryption Script Part 2 of 3

# This code was fixed based on Marco's demo
# "Message encryption" and "Message decryption" were commented out since we want to test only o folder and its contents encryption/decryption

import os
from os.path import exists
from cryptography.fernet import Fernet

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
def file_encryption(file_location, key):
    f = Fernet(key)
    with open(file_location, "rb") as file:
        data = file.read()
    encrypt_file = f.encrypt(data)
    with open(file_location, "wb") as file:
        file.write(encrypt_file)

# File decryption function
def file_decryption(file_location, key):
    f = Fernet(key)
    with open(file_location, "rb") as file:
        data = file.read()
        decrypt_file = f.decrypt(data)
    with open(file_location, "wb") as file:
        file.write(decrypt_file)

# Message encryption function
# def message_encryption():
#     message = input("\nEnter a message to encrypt: ")
#     encrypt_message = message.encode()
#     f = Fernet(key)
#     encrypt_version = f.encrypt(encrypt_message)
#     print("\nHere is the encrypted message: ")
#     print(encrypt_version)

# Message decryption function
# def message_decryption():
#     message = input("\nEnter a message to decrypt: ")
#     decrypt_message = str.encode(message)
#     f = Fernet(key)
#     decrypt_version = f.decrypt(decrypt_message)
#     print("\nHere is the encrypted message: ")
#     print(decrypt_version)

# Folder encryption function
def folder_encryption(dir_location, key):
    for root, dirs, files in os.walk(dir_location, topdown=True):
        for file_name in files:
            path = os.path.join(root, file_name)
            file_encryption(path, key)
    
# Folder decryption function
def folder_decryption(dir_location, key):
    for root, dirs, files in os.walk(dir_location, topdown=True):
        for file_name in files:
            path = os.path.join(root, file_name)
            file_decryption(path, key)

# Menu function
def menu():
    print("\nHere are your 2 options: ")
    print("\nNOTE: To decrypt a folder, you need to make sure it was previously encrypted ")
    print("\nTo encrypt a folder, select 1")
    print("To decrypt a folder, select 2")
    user_choice = input("\nMake a selection now: ")
    dir_location = input("\nProvide the path to your folder: ")

    if user_choice == "1":
        folder_encryption(dir_location, key)
        print("\nThe folder and its contents were encrypted")
    elif user_choice == "2":
        folder_decryption(dir_location, key)
        print("\nThe folder and its contents were decrypted")
    else:
        print("\nInappropriate selection!")

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
        print("\nEnjoy your day!\n")
        break
