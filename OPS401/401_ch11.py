#!/usr/bin/python3

# Script Name:                  Challenge 11
# Author:                       Mack Dirks
# Date of latest revision:      07/24/2023
# Purpose:                      Network Security Tool with Scapy Part 1 of 3

# Based on Marco's Demo
# Debugged with ChatGPT

import sys
from scapy.all import sr1, IP, ICMP, TCP


host="scanme.nmap.org"
port_range = range(20, 81)
source_port = 22

p=sr1(IP(dst=host)/ICMP())
if p:
    p.show()

for destination_port in port_range:
    # TCP packet
    response = sr1(IP(dst=host)/TCP(sport=source_port, dport=destination_port, flags="S"), timeout=1, verbose=0)
    print(response)

    # Check whether the response is a TCP packet
    if(response != None and response.haslayer(TCP)):
        # Get all the flags and ompare them to 0x12
        if(response.getlayer(TCP).flags == 0x12):
            send_rst = sr1(IP(dst=host)/TCP(sport=source_port, dport=destination_port, flags="R"), timeout=1, verbose=0)
            print(f"\n{host}:{destination_port} is open")
        # Check for 0x14 and notify the user
        elif(response.getlayer(TCP).flags == 0x14):
            print(f"\n{host}:{destination_port} is closed")
    # Check if no flag is received
    else:
        print(f"\n{host}:{destination_port} is filtered and silently dropped")