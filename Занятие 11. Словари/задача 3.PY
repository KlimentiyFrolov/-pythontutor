#http://pythontutor.ru/lessons/dicts/problems/usa_elections/
a = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    a[candidate] = a.get(candidate, 0) + int(votes)
 
for candidate, votes in sorted(a.items()):
    print(candidate, votes)