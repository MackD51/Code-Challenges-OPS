#!/bin/bash

# Script Name:                          Arrray Practice       
# Author:                               Mack Dirks                       
# Date of latest revision:              04/27/2023     
# Purpose:                              Create an Array with 4 directories 

# Declaration of variables:             

#creating an array called penguins with 4 elements
penguins=("penguin1" "penguin2" "penguin3" "penguin4")

# Declaration of functions:             

# Main

#creating a directory inside the first element of the array
mkdir "${penguins[0]}"
penguins[0]="penguin1"

#creating a directory inside the second element of the array
mkdir "${penguins[1]}"
penguins[1]="penguin2"

#creating a directory inside the third  element of the array
mkdir "${penguins[2]}"
penguins[2]="penguin3"

#creating a directory inside the forth element of the array
mkdir "${penguins[3]}"
penguins[3]="penguin4"

#using touch command to create a file
#creating a file named "sneakypenguin" inside the directory that is located inside the first element of our array
touch "${penguins[0]}/sneakypenguin.txt"

#using touch command to create a file
#creating a file named "slipperypenguin" inside the directory that is located inside the second element of our array
touch "${penguins[1]}/slipperypenguin.txt"

#using touch command to create a file
#creating a file named "spookypenguin" inside the directory that is located inside the third element of our array
touch "${penguins[2]}/spookypenguin.txt"

#using touch command to create a file
#creating a file named "sociopathicpenguin" inside the directory that is located inside the forth element of our array
touch "${penguins[3]}/sociopathicpenguin.txt"

# End