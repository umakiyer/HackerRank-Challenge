# Fun with anagrams
# https://www.codewars.com/kata/fun-with-anagrams
# By: Osvaldo A. Ramirez
# 2019-10-28
# Language: Python3
# Tested on: Python 3.7.4
# Time to solve: 0:15:00
# Tags: strings, anagrams, fun, codewars
# Resources:
# https://www.codewars.com/kata/fun-with-anagrams/discuss/python
def fun_with_anagrams(text):
    text = text.split()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            if sorted(text[i]) == sorted(text[j]):
                text[j] = ''
    return sorted(filter(None, text))
# Test
print(fun_with_anagrams('code wars code code'))
