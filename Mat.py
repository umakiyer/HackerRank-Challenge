#Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Input Format
# A single line containing the space separated values of  and .
# Constraints
# Output Format
# Output the design pattern.
# Sample Input
# 9 27
# Sample Output
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# Input (stdin)
# 9 27
# Your Output (stdout)
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# Expected Output
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# Explanation
# The design pattern shown above is for 9 X 27 size.
a=input().split()
n=int(a[0])
m=int(a[1])
for i in range(1,n,2):
    print((".|."*i).center(m,"-"))  
print("WELCOME".center(m,"-"))
for i in range(n-2,-1,-2):
    print((".|."*i).center(m,"-"))
    

    