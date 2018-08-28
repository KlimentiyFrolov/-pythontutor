#http://pythontutor.ru/lessons/while/problems/seq_index_of_max/
b = 0
a = -1
d = -1
c = 0
while d != 0:
    d = int(input())
    if d > b:
        b = d
        a = c
    c += 1
print(a)