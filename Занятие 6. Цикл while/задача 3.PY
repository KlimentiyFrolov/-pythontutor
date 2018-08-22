#http://pythontutor.ru/lessons/while/problems/powers_of_two/

a = int(input())

b = 2
c = 1

while b <= a:

    b *= 2

    c += 1

print(c - 1, b // 2)