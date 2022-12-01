from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,num):
    queue = deque([[i,j]])
    visit[i][j] = True
    board[i][j] = num
    position = []
    while queue:
        y,x = queue.popleft()
        position.append([y,x])
        for i in range(4):
            ky,kx = y + dy[i], x + dx[i]
            if 0 <= kx < n and 0 <= ky < n and visit[ky][kx] == False and board[ky][kx] != 0:
                board[ky][kx] = num
                visit[ky][kx] = True
                queue.append([ky, kx])

    return position

def bfs2(val,position):
    global answer
    dist = [[-1 for j in range(n)] for i in range(n)] # 거리가 저장될 배열
    queue = deque()

    for y,x in position:
        queue.append([y, x])
        dist[y][x] = 0

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ky,kx = y + dy[i], x + dx[i]
            if kx < 0 or kx >= n or ky < 0 or ky >= n:
                continue

            if board[ky][kx] > 0 and board[ky][kx] != val:
                answer = min(answer, dist[y][x])
                return

            if board[ky][kx] == 0 and dist[ky][kx] == -1:
                dist[ky][kx] = dist[y][x] + 1
                queue.append([ky, kx])


n = int(input())
board = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
visit = [[False for i in range(n)] for j in range(n)]

position = []
num=1

for i in range(n):
    for j in range(n):
        if visit[i][j] == False and board[i][j] == 1:
            position.append(bfs(i,j,num))
            num+=1
            
answer = 200
for i in range(1,num):
    bfs2(i,position[i-1])
print(answer)