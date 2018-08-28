#http://pythontutor.ru/lessons/while/problems/seq_second_max/
a = int(input())
b = int(input())
if a < b:
    a, b = b, a
c = int(input())
while c != 0:
    if c > a:
        b, a = a, c
    elif c > b:
        b = c
    c = int(input())
print(b)