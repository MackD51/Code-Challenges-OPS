#!/bin/bash

# Script Name:                  Challenge 9
# Author:                       Mack Dirks
# Date of latest revision:      05/04/2023
# Purpose:                      Log Retrieval via Powershell

# Declaration of variables

# Declaration of functions


# Main


#Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt

$Begin = Get-Date -Date '05/04/2023 03:00:00'
$End = Get-Date -Date '05/05/2023 03:00:00'
Get-EventLog -LogName System -After $Begin -Before $End | Out-File -FilePath "C:\Users\guns4\OneDrive\Desktop\last_24.txt"

#Output all “error” type events from the System event log to a file on your desktop named errors.txt
Get-EventLog -LogName System -EntryType Error | Out-File -FilePath "C:\Users\guns4\OneDrive\Desktop\errors.txt"

#Print to the screen all events with ID of 16 from the System event log
Get-EventLog -LogName System -InstanceId 16

#Print to the screen the most recent 20 entries from the System event log

Get-EventLog -LogName System -Newest 20

#Print to the screen all sources of the 500 most recent entries in the System event log

$Events = Get-EventLog -LogName System -Newest 500
$Events | Select-Object -ExpandProperty Source

# End