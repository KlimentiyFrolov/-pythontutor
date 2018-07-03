#http://pythontutor.ru/lessons/int_and_float/problems/sum_of_digits/
x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10
print(a + b + c)