#http://pythontutor.ru/lessons/functions/problems/length_of_segment/

import math
x
1=float(input())

y1=float(input())

x2=float(input())

y2=float(input())


def distance(x1, y1, x2, y2):

    return math.sqrt(((x1-x2)**2)+(y1-y2)**2)

    
print(distance(x1, y1, x2, y2))