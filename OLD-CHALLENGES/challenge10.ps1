#!/bin/bash

# Script Name:                  Challenge 10
# Author:                       Mack Dirks
# Date of latest revision:      05/05/2023
# Purpose:                      System Process Commands

# Declaration of variables

# Declaration of functions

# Main

#Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object -Property CPU -Descending

#Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object -Descending Id

#Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5

#Start a browser process (such as Google Chrome or MS Edge) and have it open
$browser = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$website = "https://owasp.org/www-project-top-ten/"
Start-Process -FilePath $browser -ArgumentList $website

#Start the process Notepad ten times using a for loop
for ($i=0; $i -lt 10; $i++) {Start-Process notepad}

#Close all instances of the Notepad
Stop-Process -Name notepad

#Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Google Chrome or MS Edge.
Get-Process
$var = Read-Host “Enter a PID you want to kill: “
Stop-Process -Id $var


# End

