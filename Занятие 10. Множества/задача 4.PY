#http://pythontutor.ru/lessons/sets/problems/occurs_before/
a = input().split()
l = set()
for elem in a:
    if elem in l:
        print('YES')
    else:
        print('NO')
        l.add(elem)
