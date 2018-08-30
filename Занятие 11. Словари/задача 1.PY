#http://pythontutor.ru/lessons/dicts/problems/occurency_index/
b = {}
for a in input().split():
    b[a] = b.get(a, 0) + 1
    print(b[a] - 1, end=' ')