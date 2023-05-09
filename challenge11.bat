# Script Name:                  Challenge 11
# Author:                       Mack Dirks
# Date of latest revision:      05/08/2023
# Purpose:                      System Process Commands

#Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

#Allow ICMP traffic
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4