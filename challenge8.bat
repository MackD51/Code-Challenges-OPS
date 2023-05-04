#!/bin/bash

# Script Name:                  Challenge 8
# Author:                       Mack Dirks
# Date of latest revision:      05/03/2023
# Purpose:                      Windows Batch Scripting

# Declaration of variables

# Declaration of functions


# Main

@echo off

set /p s=Enter the source Folder path (where you want to copy from): 

set /p d=Enter your Folder destination path (where you want it to copy):

ROBOCOPY "%s%" "%d%" /S

echo Your folder together with all the files were saved in the provided destination

pause



# Command I've used in the PowerShell: .\challenge8.bat



# I've tried this script first on my own computer, and it worked perfectly fine:

# @echo off

# ROBOCOPY C:\Users\md51\Favorites\Folder C:\Users\md51\Documents\New"

# pause



# End