#http://pythontutor.ru/lessons/for_loop/problems/sum_of_factorials/
n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)