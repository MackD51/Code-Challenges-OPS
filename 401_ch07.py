#!/usr/bin/python3

# Script Name:                  Challenge 07
# Author:                       Mack Dirks
# Date of latest revision:      07/18/2023
# Purpose:                      File Encryption Script Part 2 of 3

import os
import cryptography.fernet as fernet



def folder_encryption(folder_location, encryption_key)
    for root, dirs, files in os.walk(folder_location):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            folder_encryption(full_path, encryption_key)
    
def folder_decryption(folder_location, encryption_key)
    for root, dirs, files in os.walk(folder_location):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            folder_encryption(full_path, encryption_key)

# Main
print("To encrypt a folder, select 1")
print("To decrypt a folder, select 2")
user_choice = input("Make a selection now: ")
folder_location = input("Provide the path to your folder: ")
encryption_key = fernet.Fernet.generate_key()

if user_choice == "1":
    folder_encryption(folder_location, encryption_key)
elif user_choice == "2":
    folder_decryption(folder_location, encryption_key)
else:
