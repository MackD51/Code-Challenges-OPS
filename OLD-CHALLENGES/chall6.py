#!/bin/bash

# Script Name:                  Challenge 6
# Author:                       Mack Dirks
# Date of latest revision:      06/07/2023
# Purpose:                      Bash in Python


# Main

import os

# Creating variables and opening a pipe to or from command cmd
whoami_command = os.popen("whoami", mode="r", buffering=- 1)
ipa_command = os.popen("ip a", mode="r", buffering=- 1)
lshw_command = os.popen("lshw -short", mode="r", buffering=- 1)

# Reading our commands' output into the variables
whoami_result = whoami_command.read()
ipa_result = ipa_command.read()
lshw_result = lshw_command.read()

# Displaying the results
print("\nwhoami output")
print("**********************************************************************************")
print(whoami_result)
print("\nip a output")
print("**********************************************************************************")
print(ipa_result)
print("\nlshw -short output")
print("**********************************************************************************")
print(lshw_result)


# End