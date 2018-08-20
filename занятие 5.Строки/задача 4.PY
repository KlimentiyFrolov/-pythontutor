#http://pythontutor.ru/lessons/str/problems/swap_two_words/
s = input()
a= s[:s.find(' ')]
b = s[s.find(' ') + 1:]
print(b + ' ' + a)