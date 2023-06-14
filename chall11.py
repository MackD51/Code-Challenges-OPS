#!/usr/bin/env python3

# Script Name:                  Challenge 11
# Author:                       Mack Dirks
# Date of latest revision:      06/13/2023
# Purpose:                      Psutil


# Main

import psutil

user_mode = psutil.cpu_times().user
kernel_mode = psutil.cpu_times().system
idle = psutil.cpu_times().idle
priority = psutil.cpu_times().nice
in_out = psutil.cpu_times().iowait
hardware_interrupt = psutil.cpu_times().irq
software_interrupt = psutil.cpu_times().softirq
other_os = psutil.cpu_times().steal
virtual_cpu_guest = psutil.cpu_times().guest

print("\nTime spent by normal processes executing in user mode:", user_mode)
print("Time spent by processes executing in kernel mode:", kernel_mode)
print("Time when system was idle:", idle)
print("Time spent by priority processes executing in user mode:", priority)
print("Time spent waiting for I/O to complete:", in_out)
print("Time spent for servicing hardware interrupts:", hardware_interrupt)
print("Time spent for servicing software interrupts:", software_interrupt)
print("Time spent by other operating systems running in a virtualized environment:", other_os)
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", virtual_cpu_guest, "\n")


# End