#!/usr/bin/env python3

# Script Name:                  Challenge 11
# Author:                       Mack Dirks
# Date of latest revision:      06/13/2023
# Purpose:                      Psutil

import requests

# Main

import requests

destination_url = input("\nEnter the destination URL: ")

print("\nHere are your options:")
print("For GET enter 1")
print("For POST enter 2")
print("For PUT enter 3")
print("For DELETE enter 4")
print("For HEAD enter 5")
print("For PATCH enter 6")
print("For OPTIONS enter 7")

user_choice = input("\nEnter your option: ")

print(f"\nRequest to be sent:\nDestination URL: {destination_url}\nHTTP Method: {user_choice}")

user_confirmation = input("\nDo you confirm this option (enter y/Y for 'yes' or n/N for 'no'): ")

if user_confirmation.lower() == "y":
    if user_choice == "1":
        response = requests.get(destination_url)
    elif user_choice == "2":
        response = requests.post(destination_url)
    elif user_choice == "3":
        response = requests.put(destination_url)
    elif user_choice == "4":
        response = requests.delete(destination_url)
    elif user_choice == "5":
        response = requests.head(destination_url)
    elif user_choice == "6":
        response = requests.patch(destination_url)
    elif user_choice == "7":
        response = requests.options(destination_url)
    else:
        print("\nInvalid option.")

    if response:
        print("\nResponse Header:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")

        if response.status_code == 200:
            print('\nSuccess!')
        elif response.status_code == 404:
            print('\nNot Found.')
    else:
        print("\nRequest failed.")
else:
    print("\nRequest canceled.")


# End