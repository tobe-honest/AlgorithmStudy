from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def check():
    visited = [[[0 for i in range(2)] for j in range(M)] for k in range(N)]
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1

    while queue:
        x,y,z = queue.popleft()

        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            kx,ky = x+dx[i], y+dy[i]

            if kx<0 or ky<0 or kx>=N or ky>=M:
                continue

            if board[kx][ky] == 1 and z == 0:
                visited[kx][ky][1] = visited[x][y][0] + 1
                queue.append([kx,ky,1])

            elif board[kx][ky] == 0 and visited[kx][ky][z]==0:
                visited[kx][ky][z] = visited[x][y][z] + 1
                queue.append([kx, ky, z])
                
    return -1


N,M = map(int,input().split())
board = []
for i in range(N):
    line = list(map(int,input()))
    board.append(line)
    line=[]

print(check())

# 베스트 코드
# 30031405	mod96	2206	벽 부수고 이동하기	맞았습니다!!	55012	2780