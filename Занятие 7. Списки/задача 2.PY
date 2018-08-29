#http://pythontutor.ru/lessons/lists/problems/even_elements/
b=input()
a=[int(b) for b in b.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')