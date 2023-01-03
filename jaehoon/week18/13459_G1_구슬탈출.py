from collections import deque
from itertools import product



    
n,m = map(int,input().split())

board = []
red,blue,hole = [],[],[]
for i in range(n):
    line = input()
    for j,val in enumerate(line):
        if val == 'R':
            red.append([i,j])
        elif val == 'B':
            blue.append([i,j])
        elif val == 'O':
            hole.append([i,j])
    board.append(line)

candidate = []

for i in product([1,2,3,4], repeat=10):
    candidate.append(i)

for case in candidate:
    print(case)