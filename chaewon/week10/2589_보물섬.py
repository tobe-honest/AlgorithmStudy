import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split(' '))
graph=list()
for i in range(r):
    graph.append(input().strip())

direction=[[0,1,-1,0],[1,0,0,-1]]
global answer
answer=list()

def bfs(x,y,visited):
    q=deque([[x,y,0]])
    visited[x][y]=True

    while q:
        x,y,time=q.popleft()
        # if graph[x][y]=='W': # bfs시작하는 for문에서 처리하면 굳이 안 넣어도 되지만 아니면 해야함(첫 시작부터 W인 경우는 밑에서 거르지 못함)
        #     continue
        for i in range(4):
            dx,dy=x+direction[0][i],y+direction[1][i]
            if 0<=dx<r and 0<=dy<c and not visited[dx][dy] and graph[dx][dy]=='L':
                visited[dx][dy]=True
                q.append([dx,dy,time+1])
    answer.append(time)

for i in range(r):
    for j in range(c):
        if graph[i][j]=='L':
            visited=[[False]*c for _ in range(r)]
            bfs(i,j,visited)
print(max(answer))