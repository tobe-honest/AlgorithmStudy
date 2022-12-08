import sys
from itertools import combinations
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split(' '))

graph,virus=list(),list()
visited=[[-1]*n for _ in range(n)] # -1 : 방문하지 않음
wall=0 # 벽이 총 몇 개 있는지
for i in range(n):
    tmp=list(map(int,input().split(' ')))
    for j in range(n):
        if tmp[j]==1: # 벽
            wall+=1
        elif tmp[j]==2: # 바이러스
            virus.append([i,j])
    graph.append(tmp)

direction=[[1,0,-1,0],[0,1,0,-1]]
def count_time(activate,visited,virus):
    q=deque([])
    for act in activate:
        q.append(virus[act])
        visited[virus[act][0]][virus[act][1]]=0 # 활성화
    max_visited=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            dx,dy=x+direction[0][i], y+direction[1][i]
            if 0<=dx<n and 0<=dy<n and visited[dx][dy]==-1:
                
                if graph[dx][dy]==0:
                    q.append([dx,dy])
                    visited[dx][dy]=visited[x][y]+1
                    max_visited=max(max_visited,visited[dx][dy]) # 완전 중요 : visited의 max는 비활성화까지 세기 때문에 0인것에 대해서만 답을 구해줌
                if graph[dx][dy]==2:
                    q.append([dx,dy])
                    visited[dx][dy]=visited[x][y]+1
                    
    if sum(visited,[]).count(-1)!=wall: # 아예 한 번도 도착하지 못하면 그대로 -1이기 때문에 벽 갯수보다 많을 것임
        return -1 # 음수값 아무거나 상관 없음 -> 도착하지 못했다는 것만 표현하면 됨
    else:
        return max_visited
answer=1e9   
for activate in list(combinations(list(range(len(virus))),m)):
    act_time=count_time(activate,[v[:] for v in visited],virus[:])
    if act_time>=0:
        answer=min(answer,act_time)
        
if answer==1e9: # 한 번도 min값이 갱신되지 않아 그대로임
    print(-1)
else:
    print(answer)