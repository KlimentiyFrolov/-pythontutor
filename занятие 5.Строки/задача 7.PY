#http://pythontutor.ru/lessons/str/problems/delete_chunk/
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)