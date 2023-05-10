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
$Address = Get-Content -Path C:\network_report.txt | Select-String -Pattern "IPv4" | Select-String -Pattern "10.0.0.*"
return $Address
}

$Result = Find-Address
Write-Output "`nIPv4 address found:"
$Result

#Remove the network_report.txt when you are finished searching it.
Remove-Item -Path C:\network_report.txt
Write-Output "`nThe file was removed."

# End

#References
#Microsoft. (2023, January 11). About Special Characters. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_special_characters?view=powershell-7.3
#Microsoft. (n.d.) Get-Content. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7.3
#Microsoft. (n.d.). Remove-Item. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.3
#Microsoft. (n.d.). Select-String. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string?view=powershell-7.3&viewFallbackFrom=powershell-7.1
#Pearson. (2013, February 15). Overview of Windows Power PowerShell 3.0. https://www.microsoftpressstore.com/articles/article.aspx?p=2201304&seqNum=2
