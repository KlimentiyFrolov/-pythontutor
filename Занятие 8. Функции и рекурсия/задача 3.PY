#http://pythontutor.ru/lessons/functions/problems/capitalize/

s = [i for i in input().split()]

for i in s:

    print(chr(ord(i[0]) - 32),i[1:], sep ='', end = ' ')