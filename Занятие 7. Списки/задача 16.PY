#http://pythontutor.ru/lessons/lists/problems/lists_queens/

desk = []

ch = 1

while len(desk) <= 7:

  desk.append([int(i) for i in input().split()])

for i in range(len(desk)):

    for k in range(i+1, len(desk)):

        if (abs(desk[i][0]-desk[k][0]) == abs(desk[i][1]-desk[k][1])) or ((desk[i][0] == desk[k][0]) or (desk[i][1] == desk[k][1])):

            ch *= 0

        else:

            ch *= 1
if ch == 1:

    print('NO')

else:

    print('YES')