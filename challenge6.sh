#!/bin/bash

# Script Name:                  Challenge 6
# Author:                       Mack Dirks
# Date of latest revision:      05/01/2023
# Purpose:                      Practice loops, arrays, and conditions

# Declaration of variables

# Declaration of functions


# Main

# Created 2 directories to test it out
mkdir directory1
mkdir directory2

#created 2 arrays: 1 with 3 directories, and 1 fith 3 files
directories=(directory1 directory2 directory3)
files=(file1 file2 file3)

#created only 1 physical file in the first directory for now
touch "${directories[0]}/${files[0]}.txt"

# Loop to check if files/directories exist or not
for i in "${!directories[@]}"; do
    if [ -d "${directories[i]}" ] && [ -f "${directories[i]}/${files[i]}.txt" ]; then
        echo "Both directory and file exist"
        echo "*********************************************"
    elif [ -d "${directories[i]}" ]; then
        touch "${directories[i]}/${files[i]}.txt"
        echo "Directory exists, and File doesn't."
        echo "Thus, ${files[i]} was created."
        echo "*********************************************"
    elif [ -f "${directories[i]}/${files[i]}.txt" ]; then
        mkdir "${directories[i]}"
        directories[i]="${directories[i]}"
        echo "File exists, and Directory doesn't."
        echo "Thus, ${directories[i]} was created."
        echo "*********************************************"
    else
        mkdir "${directories[i]}"
        touch "${directories[i]}/${files[i]}.txt"
        echo "Both Directory and File don't exist."
        echo "Both ${directories[i]} and ${files[i]} were created."
        echo "*********************************************"
    fi
done


# End