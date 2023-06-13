#!/usr/bin/env python3

# Script Name:                  Challenge 10
# Author:                       Mack Dirks
# Date of latest revision:      06/12/2023
# Purpose:                      Python File Handling

import os

# Main

# Creates a new .txt file
new_file = open("file.txt", "w")

# Appends three lines
new_file.write("Hello world 1\n")
new_file.write("Hello world 2\n")
new_file.write("Hello world 3\n")

new_file.close()

# Prints to the screen the first line (calling readline() function only once)
new_file = open("file.txt", "r")
first_line = new_file.readline()
print("\n", first_line)

new_file.close()

# Deletes the .txt file
os.remove("file.txt")