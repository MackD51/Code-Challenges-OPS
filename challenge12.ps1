# Script Name:                  Challenge 12
# Author:                       Mack Dirks
# Date of latest revision:      05/09/2023
# Purpose:                      Powershell IP Analysis

# Main

#Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
ipconfig /all >C:\network_report.txt

#Use Select-String to search network_report.txt and return only the IP version 4 address:
function Find-Address
{
$Address = Get-Content -Path C:\network_report.txt | Select-String -Pattern "IPv4"
return $Address
}

$Result = Find-Address
Write-Output "`nIPv4 address found:"
$Result

#Remove the network_report.txt when you are finished searching it.
Remove-Item -Path C:\network_report.txt
Write-Output "`nThe file was removed."

# End

