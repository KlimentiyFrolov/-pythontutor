#http://pythontutor.ru/lessons/int_and_float/problems/konec_urokov/
a = int(input())
a = a*45 + (a//2)*5 + ((a+1)//2-1)*15
print(a//60 + 9, a%60)