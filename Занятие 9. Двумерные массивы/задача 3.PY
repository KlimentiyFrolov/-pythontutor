#http://pythontutor.ru/lessons/2d_arrays/problems/chessboard/

n, m = [int(s) for s in input().split()]

symbol = ['.', '*']

a = [ [symbol[(i%2)^(j%2)]
for row in a:

    print(' '.join(str(i) for i in row))
