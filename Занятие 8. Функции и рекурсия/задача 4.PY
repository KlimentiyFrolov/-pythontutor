#http://pythontutor.ru/lessons/functions/problems/power_rec/

def power(a,n):

    if n==0:

        return 1

    else:

        return a*power(a,n-1)

a=float(input())

n=int(input())

power(a,n)

print(power(a,n))
