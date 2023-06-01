#!/bin/bash

# Script Name:                  Challenge 2
# Author:                       Mack Dirks
# Date of latest revision:      05/31/2023
# Purpose:                      Append; Date and Time



# Main


today=$(date +%Y-%m-%d)

new_file="syslog_${today}.log"

cp /var/log/syslog "${new_file}"

echo "Copied syslog to ${new_file}"

# End
