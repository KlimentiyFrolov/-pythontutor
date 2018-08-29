#http://pythontutor.ru/lessons/lists/problems/insert_element/
a = [int(el) for el in input().split()]

b = [int(el) for el in input().split()]

for i in range(b[0], len(a)) :
 
   b[1], a[i] = a[i], b[1]

a.append(b[1]);

print(" ".join(str(el) for el in a))