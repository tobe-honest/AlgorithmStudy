from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global num
    queue = deque([[i,j]])
    visit[i][j] = True
    board[i][j] = num

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ky,kx = y + dy[i], x + dx[i]
            if ky<0 or kx<0 or ky>=n or kx >= n or visit[ky][kx]==True or board[ky][kx]==0:
                continue
            board[ky][kx] = num
            visit[ky][kx] = True
            queue.append([ky, kx])


def bfs2(val):
    global answer
    dist = [[-1 for j in range(n)] for i in range(n)] # 거리가 저장될 배열
    queue = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == val:
                queue.append([i, j])
                dist[i][j] = 0

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
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

visit = [[False for i in range(n)] for j in range(n)]
num=1
for i in range(n):
    for j in range(n):
        if visit[i][j] == False and board[i][j] == 1:
            bfs(i,j)
            num+=1
            

answer = 200
for i in range(1,num+1):
    bfs2(i)
print(answer)