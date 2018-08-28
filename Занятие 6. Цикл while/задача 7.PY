#http://pythontutor.ru/lessons/while/problems/seq_sum/

a = int(input())

b = 0

c = 0

while a != 0:

    b = b + 1

    c = c + a

    a = int(input())

b = c / b

print(b)
