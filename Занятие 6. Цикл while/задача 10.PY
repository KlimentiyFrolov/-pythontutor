#http://pythontutor.ru/lessons/while/problems/seq_num_even/
a = int(input())
c = 0
while a != 0:
    if a % 2 == 0:
        c = c + 1
    a = int(input())
print(c)