#!/bin/bash

# Script Name:                  Challenge 3
# Author:                       Mack Dirks
# Date of latest revision:      06/01/2023
# Purpose:                      File Permissions


# Main

read -p "Provide the directory path: " dir_path
read -p "Provide the permission number: " perm

cd "$dir_path"

chmod -r "$perm" .

echo "Displaying the directory contents: "

ls -l "$dir_path"

# End
