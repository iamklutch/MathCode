#!/usr/bin/env python3
"""We are given a string and we need to reverse
words of a given string

Examples:

Input : str =" geeks quiz practice code"
Output : str = code practice quiz geeks  
Input : str = "my name is laxmi"
output : str= laxmi is name my 
"""
user_string = input("Please enter a string:")
reversed_string = str()

# this is needed to keep the words together 
# otherwise it will do it by character
user_string = user_string.split(" ")

for word in user_string:
  reversed_string = word + " " + reversed_string

print(reversed_string)

