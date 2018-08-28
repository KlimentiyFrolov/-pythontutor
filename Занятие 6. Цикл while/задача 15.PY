#http://pythontutor.ru/lessons/while/problems/is_fibonacci/
a = int(input())
if a == 0:
    print(0)
else:
    b, c = 0, 1
    n = 1
    while c <= a:
        if c == a:
            print(n)
            break
        b, c = c, b + c
        n += 1
    else:
        print(-1)