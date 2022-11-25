from collections import deque
import sys
input=sys.stdin.readline
direction=[[0,1,0,-1],[1,0,-1,0]]
n,m=map(int,input().split(' '))
graph=[]
ground=set()
for i in range(n):
    tmp=list(map(int,input().split(' ')))
    for j in range(len(tmp)):
        if tmp[j]>0:
            ground.add((i,j))
    graph.append(tmp)

def melt(graph,ground):
    new_graph=[g[:] for g in graph]
    del_ground=[]
    for g in ground:
        i,j=g[0],g[1]
        for di in range(4):
            dx,dy=i+direction[0][di],j+direction[1][di]
            if 0<=dx<n and 0<=dy<m and graph[dx][dy]<=0:
                new_graph[i][j]-=1
                if new_graph[i][j]<1:
                    del_ground.append((i,j))
    for dg in del_ground:
        ground.discard(dg)

    return new_graph,ground

def bfs(x,y,graph,visited):
    q=deque([[x,y]])
    visited[x][y]=True
    while q:
        x,y=q.popleft()
        for i in range(4):
            dx,dy=x+direction[0][i],y+direction[1][i]
            if 0<=dx<n and 0<=dy<m and not visited[dx][dy] and graph[dx][dy]>0:
                q.append([dx,dy])
                visited[dx][dy]=True
    return visited

def count(graph,ground):
    visited=[[False]*m for _ in range(n)]
    cnt=0
    for g in ground:
        i,j=g[0],g[1]
        if not visited[i][j]:
            visited=bfs(i,j,graph,visited)
            cnt+=1
    return cnt
island=0
time=0
while island<2:
    time+=1
    graph,ground=melt(graph,ground)
    island=count(graph,ground)
    if island==0:
        time=0
        break
print(time)