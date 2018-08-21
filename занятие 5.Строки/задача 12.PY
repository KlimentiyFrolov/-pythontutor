#http://pythontutor.ru/lessons/str/problems/delete_every_third_char/
s = input()
a = ''
for i in range(len(s)):
    if i % 3 != 0:
        a = a + s[i]
print(a)
