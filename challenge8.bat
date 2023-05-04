#!/bin/bash

# Script Name:                  Challenge 8
# Author:                       Mack Dirks
# Date of latest revision:      05/03/2023
# Purpose:                      Windows Batch Scripting

# Declaration of variables

# Declaration of functions


# Main

@echo off

set source="C\Users\md51\Desktop\Folder"

set destination="C\Users\md51\Documents\Copy_Folder"

robocopy %source% %destination% /E

echo Your folder was saved automatically

pause


# End