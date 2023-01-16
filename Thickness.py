#You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
#Your task is to replace the blank (______) with rjust, ljust or center.
#Input Format
#A single line containing the thickness value for the logo.
#Constraints
#The thickness must be an odd number.
#Output Format
#Output the desired logo.
#Sample Input
#5
#Sample Output
#    H
#   HHH
#  HHHHH
# HHHHHHH
#HHHHHHHHH
# HHHHHHH
#  HHHHH
#   HHH
#    H
#Explanation
#The thickness must be 5, so the logo is of the length 9. Thus, the number of H's on each line is 1, 3, 5, 7 and 9. The middle line of the logo is 9 H's long and the rest of the lines are centered and padded with underscores.
#rjust, ljust or center
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    