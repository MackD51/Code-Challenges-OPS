#!/usr/bin/python3

# Script Name:                  Challenge 06
# Author:                       Mack Dirks
# Date of latest revision:      07/18/2023
# Purpose:                      File Encryption Script Part 1 of 3

# Imports cryptographic library
from cryptography.fernet import Fernet

# File encryption function
def file_encryption()
    key = Fernet.generate_key()
    f = Fernet(key)

# File decryption function
def file_decryptio()
    key = Fernet.generate_key()
    f = Fernet(key)

# Message encryption function
def message_encryption()
    key = Fernet.generate_key()
    f = Fernet(key)

# Message decryption function
def message_decryption()
    key = Fernet.generate_key()
    f = Fernet(key)

# Creates a menu with 4 different options
print("Here are your 4 options: \n")
print("To Encrypt a File, select 1\n")
print("To Decrypt a File, select 2\n")
print("To Encrypt a Message, select 3\n")
print("To Decrypt a Message, select 4\n")
