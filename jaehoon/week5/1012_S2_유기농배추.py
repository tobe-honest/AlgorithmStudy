from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(y,x):
    queue = deque([[y,x]])
    visit[y][x] = True

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ky,kx = y+dy[i] , x+dx[i]
            if ky<0 or kx<0 or ky>=N or kx>=M or visit[ky][kx] == True or board[ky][kx] == 0:
                continue

            board[ky][kx] = 1
            visit[ky][kx] = True
            queue.append([ky,kx])


T = int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    board = [[0 for col in range(M)] for row in range(N)]
    visit = [[False for col in range(M)] for row in range(N)]
    cnt = 0
    for j in range(K):
        x,y = map(int,input().split())
        board[y][x] = 1

    for y in range(N):
        for x in range(M):
            if board[y][x] == 1 and visit[y][x] == False:
                check(y,x)
                cnt+=1
    print(cnt)

