import sys
from collections import deque

n, m= map(int, sys.stdin.readline().split(' '))
graph=list()
tmp_list=list()
for _ in range(n):
    tmp=sys.stdin.readline()
    tmp_list=list()
    for t in tmp:
        if t !='\n':
            tmp_list.append(int(t))
    graph.append(tmp_list)

visited=[[[0] * 2 for _ in range(m)] for _ in range(n)]
direction=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(x,y,dist,is_broken):
    q=deque([[x,y,dist,is_broken]])
    if graph[x][y]== 1:
        visited[x][y][1]=1
    else:
        visited[x][y][0]=1
        
    while q:
        x,y,dist,is_broken=q.popleft()
        # 종료조건
        if x == n-1 and y == m-1:
            return dist

        if visited[x][y][1]>0: # 부순 상태에서 방문했음
            if visited[x][y][0] < visited[x][y][1] and visited[x][y][0]>=1: # 부수지 않고도 같은칸에 도달하는 비용이 더 적거나 같으면'

                continue

        # 큐에 추가
        for i in range(4):
            next_x, next_y =x+direction[i][0], y+direction[i][1]
            if next_x>=0 and next_x<n and next_y>=0 and next_y<m: # 범위 체크
                if graph[next_x][next_y] == 0: # 벽이 아니면
                    if is_broken:
                        if visited[next_x][next_y][1]==0: # 방문 안 함
                            q.append([next_x,next_y,dist+1,is_broken])
                            visited[next_x][next_y][1]=dist+1
                    else:
                        if visited[next_x][next_y][0]==0: # 방문함
                            q.append([next_x,next_y,dist+1,is_broken])
                            visited[next_x][next_y][0]=dist+1
                else: # 벽이면
                    if is_broken==False: # 벽을 부순적이 없다
                        q.append([next_x,next_y,dist+1,True]) # 이제 벽을 부쉈으니 True로 바꿔줘야함
                        visited[next_x][next_y][1]=dist+1
    return -1
print(bfs(0,0,1,False))
