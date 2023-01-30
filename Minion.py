# Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem
# By: Osvaldo A. Ramirez
# 2019-10-28
# Language: Python3
# Tested on: Python 3.7.4
# Time to solve: 0:15:00
# Tags: strings, substrings, game, minion, kevin, stuart
# Resources:
# https://www.hackerrank.com/challenges/the-minion-game/forum/comments/100000
String = input()
Vowels = 'AEIOU'
Stuart = 0
Kevin = 0
for i in range(len(String)):
    if String[i] in Vowels:
        Kevin += len(String) - i
    else:
        Stuart += len(String) - i
if Stuart > Kevin:
    print('Stuart', Stuart) 
elif Kevin > Stuart:
    print('Kevin', Kevin)
else:
    print('Draw')
    