#!/bin/bash

# Script Name:                  OPS Challenge 13
# Author:                       Mack Dirks
# Date of latest revision:      05/10/2023
# Purpose:                      Domain Analyzer

# Declaration of variables

# Declaration of functions


# Main

file="domain_information.txt"
user_input
{
    echo "Enter a domain name (ex. google.com): "
    read domain_name
    whois $domain_name
    dig $domain_name
    host $domain_name
    nslookup $domain_name
}



# End