#http://pythontutor.ru/lessons/lists/problems/swap_min_and_max/

s = [int(i) for i in input().split()]

n = s[0]

a = s[0]

m = 0
l = 0
k = 0

for i in range(len(s)):

    if s[i] > n:

        n = s[i]

        k = m

    elif s[i] < a:

        a = s[i]

        l = m
    m += 1
s[k], s[l] = s[l], s[k]
print(' '.join([str(j) for j in s]))