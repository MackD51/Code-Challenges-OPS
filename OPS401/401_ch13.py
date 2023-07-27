#!/usr/bin/python3

# Script Name:                  Challenge 13
# Author:                       Mack Dirks
# Date of latest revision:      07/26/2023
# Purpose:                      Network Security Tool with Scapy Part 3 of 3

# Based on Marco's Demo
# Debugged with ChatGPT

# Import libraries
import sys
from scapy.all import sr1, sr, IP, ICMP, TCP
import ipaddress
import random

#Define functions

# TCP Port scan function
def tcp_scan(host):
    #range to test it
    port_range = [22, 23, 80, 443, 3389]

    for destination_port in port_range:
        source_port = random.randint(1025, 65533)
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


# ICMP ping sweep
def icmp_check(host):
    response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

    if response != None:
        if (int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            print(f"\n{host} is actively blocking ICMP traffic")
        else:
            print(f"\n{host} is responding")
            tcp_scan(host)
    else:
        print(f"\n{host} is down")



#Main

while True:
    host = input("\nProvide an IP address to scan: ")
    print("\n***************************************************************")
    icmp_check(host)
    print("\n***************************************************************")
    answer = input("\nDo you want to try again? yes or no: ")
    if answer == "no":
        print("\nEnjoy your day!\n")
        break


