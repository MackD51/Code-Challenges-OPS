#!/bin/bash

# Script Name:                  Challenge 10
# Author:                       Mack Dirks
# Date of latest revision:      05/05/2023
# Purpose:                      System Process Commands

# Declaration of variables

# Declaration of functions

# Main

#Print to the terminal screen all active processes 
#ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object -Property CPU -Descending

#Print to the terminal screen all active processes ordered by 
#highest Process Identification Number at the top.
Get-Process | Sort-Object -Descending Id

# End

