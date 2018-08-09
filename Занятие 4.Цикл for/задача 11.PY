#http://pythontutor.ru/lessons/for_loop/problems/lost_card/
n = int(input())
a = 0
for i in range(1, n + 1):
    a += i
for i in range(n - 1):
    a -= int(input())
print(a)