#!/bin/bash

# Script Name:                  Challenge 7
# Author:                       Mack Dirks
# Date of latest revision:      05/05/2023
# Purpose:                      System Information

# Declaration of variables

# Declaration of functions


# Main

echo NAME OF THE COMPUTER:
sudo hostname

echo "*******************************************************************************************"
echo CPU Info:
sudo lshw | grep *-cpu -A 6 | grep -v "version"

echo "*******************************************************************************************"
echo RAM Info:
sudo lshw | grep *-memory -A 3

echo "*******************************************************************************************"
echo Adapter Info:
sudo lshw | grep *-display -A 12 | head -6 
sudo lshw | grep *-display -A 12 | tail -5

echo "*******************************************************************************************"
echo Network Adapter Info:
sudo lshw | grep *-network -A 15


# End