#http://pythontutor.ru/lessons/lists/problems/num_distinct/

a = list(map(int, input().split(" ")))

count = 1

for i in range(1, len(a)):

    if a[i - 1] != a[i]:

        count += 1
print(count)
