#You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
s=input()
print(any(c.isalnum() for c in s))
print(any(c
.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c
.islower() for c in s))
print(any(c
.isupper() for c in s))

