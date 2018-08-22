#http://pythontutor.ru/lessons/while/problems/minimal_divisor/
a = int(input())
i = 2
while a % i != 0:
    i += 1
print(i)