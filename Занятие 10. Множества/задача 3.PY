#http://pythontutor.ru/lessons/sets/problems/sets_intersection/

print(*sorted(set(input().split()) & set(input().split()), key=int))