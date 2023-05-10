# Script Name:                  Challenge 12
# Author:                       Mack Dirks
# Date of latest revision:      05/09/2023
# Purpose:                      Powershell IP Analysis

# Main

#Create a local file called network_report.txt that holds the contents of an ipconfig /all command.
ipconfig /all >C:\network_report.txt

find_address
{
$address = Get-Content -Path .\network_report.txt | Select-String -Pattern "IPv4"
return $address
}

result = find_address

Write-Output IPv4 address found:

$result

Remove-Item -Path .\network_report.txt

# End