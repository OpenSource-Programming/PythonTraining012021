# Exercise 1: Write a simple program to simulate the operation of the grep com-
# mand on Unix. Ask the user to enter a regular expression and count the number
# of lines that matched the regular expression:

# Import the module
import re

# Enter File Name
filename = input("Enter the filename: ")
# Enter Regular Expression
regex = input("Enter a regular expression: ")

# Find and store the count of the seach Word

counter = 0
fhand = open(filename, 'r')
for line in fhand:
    line = line.rstrip()
    if re.search(regex, line):
        counter += 1

print(counter)