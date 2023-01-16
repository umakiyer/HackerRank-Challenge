#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
#Given a full name, your task is to capitalize the name appropriately.
#Input Format
#A single line of input containing the full name, .
#Constraints
#The string consists of alphanumeric characters and spaces.
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
#Output Format
#Print the capitalized string, .
#Sample Input
#chris alan
#Sample Output
#Chris Alan
#Explanation
#There are three names in the input. The first name is capitalized correctly, the second name is capitalized, and the last name is not capitalized. Hence, the output is Chris Alan.
#Solution:
#!/usr/bin/env python3
# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s    

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
