#!/bin/bash

# Script Name:                  Challenge 13
# Author:                       Mack Dirks
# Date of latest revision:      06/16/2023
# Purpose:                      Powershell AD Automation

# Declaration of variables

$firstName = "Franz"
$lastName = "Ferdinand"
$name = "Franz Ferdinand"
$title = "TPS Reporting Lead"
$email = "ferdi@GlobeXpower.com"
$company = "GlobeX USA"
$office = "Springfield, OR"
$department = "TPS Department"

$password = ConvertTo-SecureString -String "solar@1234" -AsPlainText -Force

# Main

#Creating our new user
New-ADUser -SamAccountName ($name.Replace(" ",".").ToLower()) -Name $name -Title $title -EmailAddress $email -Company $company -Office $office -Department $department -Enabled $true -AccountPassword $password -GivenName $firstName -Surname $lastName

Write-Host "`nUser $name was created successfully"

#Testing
Get-ADUser -Identity "franz.ferdinand"

# End