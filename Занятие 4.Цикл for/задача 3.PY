#http://pythontutor.ru/lessons/for_loop/problems/series_3/
A =int(input(""))
B =int(input(""))
if A%2==0:
    A-=1
if B%2:
    B-=1
for i in range(A, B, -2):
    print(i, end=' ')