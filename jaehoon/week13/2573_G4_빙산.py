from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(board,i,j,visit,n,m):
    queue = deque([[i,j]])
    visit[i][j] = True

    while queue:
        y,x = queue.popleft()
        for i in range(4):
            ky,kx = y + dy[i], x + dx[i]
            if kx < 0 or ky <0 or kx >= m or ky >= n or visit[ky][kx] == True or board[ky][kx] == 0:
                continue
            visit[ky][kx] = True
            queue.append([ky, kx])

    return visit

def count_piece(board,n,m,ice):
    visit = [[False for j in range(m)] for i in range(n)]
    cnt = 0
    for i in ice:
        y,x = i[0], i[1]
        if visit[y][x] == False:
            visit = bfs(board,y,x,visit,n,m)
            cnt+=1

    return cnt


def melting(board,n,m,ice):
    temp = [ b[:] for b in board]
    idx = []
    for i in ice:
        y,x,cnt = i[0], i[1], 0
        for j in range(4):
            ky,kx = y + dy[j], x + dx[j]
            if 0 <= kx < m and 0 <= ky < n and temp[ky][kx] == 0:
                cnt+=1
        board[y][x] = max(0,temp[y][x]-cnt)
        if board[y][x] == 0:
            idx.append((y,x))

    ice = list(set(ice) - set(idx))

    return board, ice
                

if __name__ == "__main__":
    n,m = map(int,input().split())
    board,ice,cnt,t = [],[],0,0
    for i in range(n):
        line = list(map(int,sys.stdin.readline().split()))
        board.append(line)
        for j in range(m):
            if line[j] > 0:
                ice.append((i,j))
    while True:
        cnt = count_piece(board,n,m,ice)
        if cnt == 0:
            print(0)
            exit()
        if cnt >= 2:
            print(t)
            exit()
        board,ice = melting(board,n,m,ice)
        t+=1

