#!/usr/bin/python3

# Script Name:                  Challenge 07
# Author:                       Mack Dirks
# Date of latest revision:      07/18/2023
# Purpose:                      File Encryption Script Part 2 of 3

import os
from cryptography.fernet import Fernet

# Function to generate the key
def gen_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as k_file:
        k_file.write(key)

# Function to load our key:
def key_load():
    return open("key.key", "rb").read

def folder_encryption(dir_location, encryption_key):
    for root, dirs, files in os.walk(dir_location):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            folder_encryption(full_path, encryption_key)
    
def folder_decryption(dir_location, encryption_key):
    for root, dirs, files in os.walk(dir_location):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            folder_decryption(full_path, encryption_key)

# Main
print("To encrypt a folder, select 1")
print("To decrypt a folder, select 2")
user_choice = input("Make a selection now: ")
dir_location = input("Provide the path to your folder: ")
encryption_key = fernet.Fernet.generate_key()

if user_choice == "1":
    folder_encryption(dir_location, encryption_key)
elif user_choice == "2":
    folder_decryption(dir_location, encryption_key)
else:
       print("Inappropriate selection!")
