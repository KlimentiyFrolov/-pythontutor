#http://pythontutor.ru/lessons/sets/problems/polyglotes/
a = [{input() for j in range(int(input()))} for i in range(int(input()))]
b, c = set.intersection(*a), set.union(*a)
print(len(b), *sorted(b), sep='\n')
print(len(c), *sorted(c), sep='\n')
