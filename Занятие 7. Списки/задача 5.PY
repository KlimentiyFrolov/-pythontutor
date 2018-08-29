#http://pythontutor.ru/lessons/lists/problems/more_than_neighbours/
a = [int(i) for i in input().split()]
b = 0
for i in range(1, len(a) - 1):
    # о боги, разве так можно писать?
    if a[i - 1] < a[i] > a[i + 1]:
        b += 1
print(b)