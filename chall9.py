#!/usr/bin/env python3

# Script Name:                  Challenge 9
# Author:                       Mack Dirks
# Date of latest revision:      06/09/2023
# Purpose:                      Python Conditional Statements


# Main


print("Enter a:")
a = int(input())
print("Enter b:")
b = int(input())

print("*********************************************")
print("Test 1:")
print("---------------------------------------------")
if a == b:
    print(a, "is equal to", b)
else:
    print(a, "is not equal to", b)

#print("---------------------------------------------")
print("\nTest 2:")
print("---------------------------------------------")
if a <= b:
    print(a, "<=", b)
    if a < b:
        print(a, "<", b)
    elif a == b:
        print(a, "=", b)
else:
    print(a, ">", b)
      
#print("---------------------------------------------")
print("\nTest 3:")
print("---------------------------------------------")
if a >= b:
    print(a, ">=", b)
    if a > b:
        print(a, ">", b)
    elif a == b:
        print(a, "=", b)
else:
    print(a, "<", b)


# End