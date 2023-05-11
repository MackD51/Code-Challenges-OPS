#!/bin/bash

# Script Name:                  OPS Challenge 13
# Author:                       Mack Dirks
# Date of latest revision:      05/10/2023
# Purpose:                      Domain Analyzer

# Declaration of variables

file="domain_information.txt"
line_separator="****************************************************************"

# Declaration of functions

user_input()
{
    echo "Enter a domain name (ex. google.com): "
    read domain_name
    {
        whois $domain_name
        echo "$line_separator"
        dig $domain_name
        echo "$line_separator"
        host $domain_name
        echo "$line_separator"
        nslookup $domain_name
    } >> $file
}

# Main

user_input

# End