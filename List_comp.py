# Let's learn about list comprehensions! 
# ou are given three integers  and  representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . 
# Please use list comprehensions rather than multiple loops, as a learning exercise.
# Input Format
# Four integers  and , each on a separate line.
# Constraints
# Print the list in lexicographic increasing order.
# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# Explanation 0
# Concept
# You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. These examples might help.
# Example: You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, .
# Concept   
x=int(input())
y=int(input())
z=int(input())
n=int(input())
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
