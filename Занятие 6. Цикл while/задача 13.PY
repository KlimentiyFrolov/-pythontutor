#http://pythontutor.ru/lessons/while/problems/seq_num_maximal/
a = 0
b = 0
c = -1
while c != 0:
    c = int(input())
    if c > a:
        a, b = c, 1
    elif c == a:
        b += 1       
print(b)
