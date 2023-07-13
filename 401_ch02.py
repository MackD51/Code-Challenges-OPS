#!/usr/bin/python3

# Script Name:                  Challenge 02
# Author:                       Mack Dirks
# Date of latest revision:      07/11/2023
# Purpose:                      Uptime Sensor Tool Part 1 of 2

# import libraries
import os 
import time
import datetime

# define function to check ping status
def ping_status(ip_test):

    # sends one ping to ip_test and assigns the result to variable
    result = os.system("ping -c 1 " + ip_test)

    # check the result
    if result == 0:
        status_msg = "host is up"
    else:
        status_msg = "host is down"
    return status_msg

# calls function, passes 8.8.8.8 as a parameter and assigns result to variable

status_msg = ping_status("8.8.8.8")

# infinite loop for constant ping

while True:
    current = datetime.datetime.now()
    print(str(current) + " " + status_msg + " to 8.8.8.8")
    time.sleep(2)


    
