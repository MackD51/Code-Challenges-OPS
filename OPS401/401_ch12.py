#!/usr/bin/python3

# Script Name:                  Challenge 12
# Author:                       Mack Dirks
# Date of latest revision:      07/25/2023
# Purpose:                      Network Security Tool with Scapy Part 2 of 3

# Based on Marco's Demo
# Debugged with ChatGPT

# Import libraries
import sys
from scapy.all import sr1, IP, ICMP, TCP
import ipaddress


#Define functions

# TCP Port scan function - ask the user for IP address to scan
def tcp_scan():
    host = input("Provide an IP address to scan: ")
    #small range to test it
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


#ICMP ping sweep
def icmp_sweep():
    cidr_block = input("Provide CIDR block subnet: ")
    ip_list = ipaddress.IPv4Network(cidr_block)
    host_count = 0

    # Send ICMP request for each host
    for host in ip_list:
        if (host in (ip_list.network_address, ip_list.broadcast_address)):
            # Skip
            print(f"Host {host} is down")
            continue
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)

        if response != None:
            if (int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                print(f"Host {host} is actively blocking ICMP traffic")

            else:
                print(f"Host {host} is responding")
                host_count = host_count + 1
    print(f"\nThere are {host_count} hosts online")


# Menu function
def menu():
    print("\nHere are your 2 options: ")
    print("\nFor TCP port scan, select 1")
    print("For ICMP ping sweep, select 2")
    user_choice = input("\nSelect your option: ")

    if (user_choice == "1"):
        tcp_scan()
    elif (user_choice == "2"):
        icmp_sweep()
    else:
        print("\nInappropriate selection!")

#Main
while True:
    menu()
    answer = input("\nDo you want to try again? yes or no: ")
    if answer == "no":
        print("\nEnjoy your day!\n")
        break


