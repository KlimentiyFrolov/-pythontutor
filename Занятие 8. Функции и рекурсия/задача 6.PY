#http://pythontutor.ru/lessons/functions/problems/fibonacci_rec/

def fib(n):

    if n==0:

        return 0

    if n==1:

        return 1

    else:

        return fib(n-1)+fib(n-2)

        

n=int(input())

print(fib(n))