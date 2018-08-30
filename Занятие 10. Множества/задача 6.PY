#http://pythontutor.ru/lessons/sets/problems/number_of_words/
words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))
