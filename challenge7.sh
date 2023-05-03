#!/bin/bash

# Script Name:                  Challenge 7
# Author:                       Mack Dirks
# Date of latest revision:      05/02/2023
# Purpose:                      System Information

# Declaration of variables

# Declaration of functions


# Main

echo Name of the computer:
sudo hostname

echo "*******************************************************************************************"
echo CPU Info:
sudo lshw -short | grep -E 'processor|product|vendor|physical id|bus info|width'

echo "*******************************************************************************************"
echo RAM Info:
sudo lshw -short | grep -E 'memory|description|physical id|size'

echo "*******************************************************************************************"
echo Adapter Info:
sudo lshw -short | grep -E 'display|description|product|vendor|physical id|bus info|width|clock|capabilities|configuration|resources'

echo "*******************************************************************************************"
echo Network Adapter Info:
sudo lshw -short | grep -E 'network|description|product|vendor|physical id|bus info|logical name|version|serial|size|capacity|width|clock|capabilities|configuration|resources'


# End