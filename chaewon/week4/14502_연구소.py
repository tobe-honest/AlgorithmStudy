from itertools import combinations
from collections import deque
import copy

n,m= map(int, input().split(' '))
graph=[list(map(int, input().split(' '))) for _ in range(n)]
empty=list() # 0 인 곳으로 벽을 세울 수 있는 후보
virus=list() # 바이러스 존재 위치 미리 저장
visited=[[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]== 0:
            empty.append((i,j))
        elif graph[i][j]==1:
            visited[i][j]=True # 벽에 대해 미리 방문 처리
        elif graph[i][j] ==2:
            virus.append([i,j])
            visited[i][j]=True # 바이러스 기존 위치에 대해 미리 방문 처리
candidates=list(combinations(empty,3)) # 비어있는 곳을 기반으로 벽을 세울 수 있는 세 곳을 조합으로 모두 만듦
direction=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs(can,graph,visited):
    q=deque(virus) # 바이러스가 존재하는 곳을 모두 큐에 넣음
    
    # 현재 graph에 대해서 벽을 미리 세워뒀기 때문에 방문처리에 벽 처리
    for c in can:
        graph[c[0]][c[1]]=1
        visited[c[0]][c[1]]=True
        
    while q:
        x,y=q.popleft()

        if graph[x][y]==1:
            continue

        for i in range(4):
            next_x, next_y= x+direction[i][0], y+direction[i][1]
            if next_x>=0 and next_x<n and next_y>=0 and next_y<m and visited[next_x][next_y]==False:
                q.append((next_x, next_y))
                graph[next_x][next_y]=2 # 바이러스 감염
                visited[next_x][next_y]=True # 방문처리

    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                cnt+=1
    return cnt

answer=list()
for can in candidates:
    now_visited=copy.deepcopy(visited)
    now_graph=copy.deepcopy(graph)
    answer.append(bfs(list(can),now_graph,now_visited))

print(max(answer))
