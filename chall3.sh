#!/bin/bash

# Script Name:                  Challenge 3
# Author:                       Mack Dirks
# Date of latest revision:      06/01/2023
# Purpose:                      File Permissions


# Main
read -p "Provide the directory path: " dir_path

perm=read "Provide the permission number: "

cd "$dir_path"

chmod "$perm" *

ls -l

stat -c



# End