#http://pythontutor.ru/lessons/int_and_float/problems/purchase_price/
a = int(input())
b = int(input())
n = int(input())
c = n * (100 * a + b)
print(c // 100, c % 100)