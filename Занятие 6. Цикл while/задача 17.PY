#http://pythontutor.ru/lessons/while/problems/std_dev/

from math import sqrt
 

a = 0

b = 0

c = int(input())

d = 0

while c != 0:

    d += 1

    a += c

    b += c ** 2

    c = int(input())

print(sqrt((b - a ** 2 / d) / (d - 1)))