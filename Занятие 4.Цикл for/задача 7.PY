#http://pythontutor.ru/lessons/for_loop/problems/factorial/
a = 1
n = int(input())
for i in range(1, n + 1):
    a *= i
print(a)