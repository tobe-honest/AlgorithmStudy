import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x, y):
    global result
    queue = set([(x, y, board[x][y])])
    while queue:
        x, y, val = queue.pop()
        for i in range(4):
            kx, ky = x + dx[i],y + dy[i]
            if ((0 <= kx < R) and (0 <= ky < C)) and (board[kx][ky] not in val):
                queue.add((kx,ky,val + board[kx][ky]))
                result = max(result, len(val)+1)

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
result = 1
BFS(0, 0)
print(result)