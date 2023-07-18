#!/usr/bin/python3

# Script Name:                  Challenge 03
# Author:                       Mack Dirks
# Date of latest revision:      07/12/2023
# Purpose:                      Uptime Sensor Tool Part 2 of 2

# Based on Marco's explanations in class

# import libraries
import os 
import time
import datetime
import smtplib
from getpass import getpass

# delacre variables
email = input("Enter email: ")
password = getpass("enter password: ")
ip_addr = input("Enter Target IP: ")
up = "ip is up"
down ="ip is down"
mailbot = "mailbot@codefellows.com"

# check status change
last_status = 0
ping_status = 0

# Delcare functions
# function to show the change from down to up
def down_to_up():

    current = datetime.datetime.now()

    smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_session.starttls()
    smtp_session.login(email, password)
    message = "Server is back up"
    smtp_session.sendmail(mailbot, email, message)
    smtp_session.quit()

# function to show the change from up to down
def up_to_down():

    current = datetime.datetime.now()

    smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_session.starttls()
    smtp_session.login(email, password)
    message = "Server is Literally on Fire!"
    smtp_session.sendmail(mailbot, email, message)
    smtp_session.quit()

# define function to check ping status
def ping_status(ip_addr):
    global ping_status
    global last_status

#     # check the result
    if ((ping_status != last_status) and (ping_status == up)):
        #overwrites whatever was in last_status
        last_status = up 
        down_to_up()
    elif ((ping_status != last_status) and (ping_status == down)):
        up_to_down(ip_addr)
        last_status = down

    result = os.system("ping -c 1 " + ip_addr)
    return last_status

# # calls function, passes ip_addr as a parameter and assigns result to variable

status_msg = ping_status("ip_addr")

# infinite loop for constant ping

while True:
    current = datetime.datetime.now()
    print(str(current) + " " + status_msg + " to ip_addr")
    time.sleep(2)
