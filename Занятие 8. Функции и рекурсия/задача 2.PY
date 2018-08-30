#http://pythontutor.ru/lessons/functions/problems/negative_power/
def power(a, n):
    b = 1
    for i in range(abs(n)):
        b *= a
    if n >= 0:
        return b
    else:
        return 1 / b
 
print(power(float(input()), int(input())))