#http://pythontutor.ru/lessons/lists/problems/lineup/
a = [int(i) for i in input().split()]
x = int(input())
b = 0
while b < len(a) and a[b] >= x:
    b += 1
print(b + 1)