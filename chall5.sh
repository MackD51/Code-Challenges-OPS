#!/bin/bash

# Script Name:                  Challenge 5
# Author:                       Mack Dirks
# Date of latest revision:      06/05/2023
# Purpose:                      Clearing Logs


# Main

log1="/var/log/syslog"
log2="/var/log/wtmp"

# Get the file sizes of log1 and log2
size1=$(stat -c "%s" "$log1")
size2=$(stat -c "%s" "$log2")

echo "Syslog size is $size1 bytes"
echo "wtmp size is $size2 bytes"

backup="/var/log/backups"
mkdir -p "$backup"

# Get the current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

file1=$(basename "$log1")
file2=$(basename "$log2")

# Compress log1
zip1="$backup/${file1}-${timestamp}.zip"
zip -q "$zip1" "$log1"
compressed1=$(stat -c "%s" "$zip1")

# Compress log2
zip2="$backup/${file2}-${timestamp}.zip"
zip -q "$zip2" "$log2"
compressed2=$(stat -c "%s" "$zip2")

echo -n > "$log1"
echo -n > "$log2"
echo -e "\nLog files were cleared"

echo -e "\nCompressed syslog size is $compressed1 bytes"
echo "Compressed wtmp size is $compressed2 bytes"

if [[ $compressed1 -lt $size1 ]]; then
    echo -e "\nCompressed syslog is smaller than the original file."
elif [[ $compressed1 -eq $size1 ]]; then
    echo -e "\nCompressed syslog is the same size as the original file."
else
    echo -e "\nCompressed syslog is larger than the original file."
fi

if [[ $compressed2 -lt $size2 ]]; then
    echo "Compressed wtmp is smaller than the original file."
elif [[ $compressed2 -eq $size2 ]]; then
    echo "Compressed wtmp is the same size as the original file."
else
    echo "Compressed wtmp is larger than the original file."
fi


# End