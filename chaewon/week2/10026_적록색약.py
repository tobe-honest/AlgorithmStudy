from collections import deque
n=int(input())

graph=list()
xgraph=list()
for _ in range(n):
    tmp=input()
    x=''
    for t in tmp:
        if t=='G':
            x+='R'
        else:
            x+=t
    graph.append(tmp)
    xgraph.append(x)

dx=[0,1,-1,0] # 우 하 상 좌
dy=[1,0,0,-1]
def bfs(graph,visited,x,y):
    target=graph[x][y]
    q=deque([(x,y,target)])
    visited[x][y]=True
    while q:
        x,y,target=q.popleft()

        for i in range(4):
            next_x=x+dx[i]
            next_y=y+dy[i]
            if next_x<n and next_x>-1 and next_y<n and next_y>-1:
                if graph[next_x][next_y]==target and visited[next_x][next_y]==False:
                    q.append((next_x,next_y,target))
                    visited[next_x][next_y]=True

    return True,target

visited=[[False for _ in range(n)] for _ in range(n)] 
xvisited=[[False for _ in range(n)] for _ in range(n)] 

result={'R':0,'G':0,'B':0}
xresult={'R':0,'B':0} 
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            is_area, color= bfs(graph,visited, i,j)
            if is_area:
                result[color]+=1
        if xvisited[i][j]==False:
            is_area, color= bfs(xgraph,xvisited, i,j)
            if is_area:
                xresult[color]+=1

print(sum(list(result.values())),sum(list(xresult.values())))
