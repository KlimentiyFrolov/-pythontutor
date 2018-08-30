#http://pythontutor.ru/lessons/dicts/problems/countries_and_cities/
a = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        a[city] = country
         
for i in range(int(input())):
    print(a[input()])