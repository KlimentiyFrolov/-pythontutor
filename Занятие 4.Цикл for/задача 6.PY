#http://pythontutor.ru/lessons/for_loop/problems/sum_of_cubes/

n = int(input())

b = 1

c = 0

for i in range(n):

    a = b * b * b

    b = b + 1

    c += a

print(c)