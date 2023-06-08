#!/usr/bin/env python3

# Script Name:                  Challenge 7
# Author:                       Mack Dirks
# Date of latest revision:      06/07/2023
# Purpose:                      Generate Directory Information

# Import libraries
import os

# Declaration of variables

# Reading a user input into a variable
user_path = input("Enter a directory path: ")

# Declaration of a function with a general parameter
def dir_info(testdir):
    for (root, dirs, files) in os.walk(testdir):
        print("\nDirectory: ", root)
        print("Sub-directories: ", dirs)
        print("Files: ", files, "\n")

# Main

# Calling the dir_creation function
# Passing the variable "path" into it
dir_info(user_path)

# End