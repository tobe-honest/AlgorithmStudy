import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque([[0,0]])

    while queue:
        y,x = queue.popleft()

        if y == n-1 and x == m-1:
            result.append(1)

        for i in range(4):
            ky,kx = y+dy[i], x+dx[i]
            if ky<0 or kx<0 or ky>=n or kx>=m or board[ky][kx] >= board[y][x]:
                continue

            queue.append([ky,kx])


n,m = map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = []
bfs()
print(len(result))
