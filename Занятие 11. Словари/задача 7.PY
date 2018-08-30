#http://pythontutor.ru/lessons/dicts/problems/english_latin_dict/
n=int(input())
d={}
for i in range(n):
    b=input().split()
    for j in range(2,len(b)):
        if b[j][len(b[j])-1]==',':
            q=1
        else:
            q=0
        if b[j][:len(b[j])-q] not in d:
            d[b[j][:len(b[j])-q]]=[]
        d[b[j][:len(b[j])-q]].append(b[0])
q=0
print(len(d))
for k,v in sorted(d.items()):
    if k[len(k)-1]==',':
        q=1
    else:
        q=0
    print(k[:len(k)-q],'-',end=' ')
    for i in range(len(v)):
        if i+1==len(v):
            print(v[i])
        else:
            print(v[i],end=', ')
