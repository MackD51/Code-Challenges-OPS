#!/bin/bash

# Script Name:                  Challenge 2
# Author:                       Mack Dirks
# Date of latest revision:      05/31/2023
# Purpose:                      Append; Date and Time



# Main


timestamp=$(date +%Y-%m-%d_%H-%M-%S)

destination_file="syslog_${timestamp}.log"

cp /var/log/syslog "${new_file}"

echo "Copied /var/log/syslog to ${new_file}"

# End