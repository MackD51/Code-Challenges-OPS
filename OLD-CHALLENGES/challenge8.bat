# Script Name:                  Challenge 8
# Author:                       Mack Dirks
# Date of latest revision:      05/03/2023
# Purpose:                      Windows Batch Scripting


# Main

#Jorge's folder was created on my Desktom with some subdirectories and files

robocopy C:\Users\md51\OneDrive\Desktop C:\Users\md51\Documents /s /logs+:jorgelogfile.txt

#If we want to make sure this backup runs only during certain times, we would add /rh:2300-0600 (or some different time window) as well

#In order to automate it, we would go to our Task Scheduler -> Create Basic Task -> would give it a name -> 
#would choose if we want it to perform once/daily/etc. -> Start Process and provide a path

# End