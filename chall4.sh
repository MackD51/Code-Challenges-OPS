#!/bin/bash

# Script Name:                  Challenge 4
# Author:                       Mack Dirks
# Date of latest revision:      06/02/2023
# Purpose:                      Conditionals in Menu Systems


# Main

function menu
{
echo -e "\nHere is the menu:"
echo -e "\nEnter 1 for Hello World"
echo "Enter 2 for Ping Self"
echo "Enter 3 for IP Info"
echo "Enter 4 to Exit"

echo -e "\nPlease enter your option: "
read user_choice

if [ $user_choice == 1 ]; then
    echo "Hello World"
elif [ $user_choice == 2 ]; then
    ping localhost
elif [ $user_choice == 3 ]; then
    ip a
else
    exit 1
fi
}

menu

echo -e "\nWould you like to see the menu (y/Y for yes, n/N for no)? "
read answer
while [ $answer == "y" ] || [ $answer == "Y" ];
do
menu
done

# End
