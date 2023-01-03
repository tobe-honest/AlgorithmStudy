from collections import deque

def bfs():
    queue = deque()


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

print(red)
print(blue)
print(hole)
    