#http://pythontutor.ru/lessons/str/problems/first_and_last_occurences/
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))