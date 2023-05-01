#!/bin/bash

# Script Name:                  Loop Practice
# Author:                       Mack Dirks
# Date of latest revision:      04/28/2023
# Purpose:                      Practice loops

# Declaration of variables

# Declaration of functions


# Main
echo "-----------------------------------------------------------------------------------"
echo You will be able to kill as many processes as you want until you exit with Ctrl+C
echo "-----------------------------------------------------------------------------------"

while :
do
echo "Displaying running processes:"
echo "-------------------------------"
ps -au

echo Enter a PID you want to kill: 
read user_input

kill -9 $user_input
echo PID $user_input was killed
echo "-------------------------------"
done

# End