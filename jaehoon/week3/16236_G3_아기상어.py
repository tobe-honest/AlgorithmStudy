from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y,board,level,count):
    visited = [[False for i in range(N)] for j in range(N)]
    visited[x][y], board[x][y] = True, 0
    queue = deque([[0,x,y]])
    candidate = []

    while queue:
        D,X,Y = queue.popleft()
        for i in range(4):
            kd, kx, ky = D+1, X+dx[i], Y+dy[i]
            if kx<0 or ky<0 or kx>=N or ky>=N or board[kx][ky]>level or visited[kx][ky] == True:
                continue
            
            visited[kx][ky] = True
            queue.append([kd,kx,ky])

            if board[kx][ky] < level and board[kx][ky]!=0:
                candidate.append([kd,kx,ky])

    if len(candidate)==0:
        return -1,-1,0,level,count
    else:
        candidate.sort()
        board[candidate[0][1]][candidate[0][2]] = 0
        count+=1
        if count==level:
            level+=1
            count=0
        return candidate[0][1],candidate[0][2],candidate[0][0],level,count

        
N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            idx,idy = i,j
            break


result,level,count = 0,2,0

while idx!=-1 and idy!=-1:
    idx,idy,time,level,count = check(idx,idy,board,level,count)
    result+=time

print(result)