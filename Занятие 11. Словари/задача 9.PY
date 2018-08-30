#http://pythontutor.ru/lessons/dicts/problems/sales/
A = {}
fname, item, n = input().split()
A[(fname, item)] = n
n = int(n)
C = {fname}
while fname != str(''):
    try:
        fname, item, n = input().split()
        n = int(n)
        C.update({fname})
        if (fname, item) not in set(A.keys()):
            A[(fname, item)] = n
        else:
            A[(fname, item)] = n + int(A[(fname, item)])
    except ValueError:
        break
for fname in sorted(C):
    print(fname + ':')
    for key in sorted(A):
        if key[0] == fname:
            print(key[1], A[key], sep = ' ')
