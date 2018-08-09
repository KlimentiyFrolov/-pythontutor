#http://pythontutor.ru/lessons/for_loop/problems/how_many_zeroes/
a = 0
for i in range(int(input())):
    if int(input()) == 0:
        a += 1
print(a)