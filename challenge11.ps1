# Script Name:                  Challenge 11
# Author:                       Mack Dirks
# Date of latest revision:      05/08/2023
# Purpose:                      Automated Endpoint Configuration

#Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

#Allow ICMP traffic
netsh advfirewall firewall add rule name="ICMPv4 Allow Ping Requests" protocol=icmpv4 dir=in action=allow

#Enable Remote management
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

#Remove bloatware
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

#Enable Hyper-V
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

#Disable SMBv1, an insecure protocol
Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol

#Resources Used:
#https://github.com/superswan/Powershell-SysAdmin
#https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3?tabs=server