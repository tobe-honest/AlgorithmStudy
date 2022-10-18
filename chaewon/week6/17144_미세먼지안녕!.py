import sys
input=sys.stdin.readline
r,c,t=map(int,input().split(' '))
graph=list()
for _ in range(r):
    graph.append(list(map(int,input().split(' '))))

ac=[] # 공기청정기
for i in range(r):
    if graph[i][0]==-1:
        ac.append(i)

direction=[[0,1],[1,0],[0,-1],[-1,0]]
def spread(graph):
    new_graph=[row[:] for row in graph]
    for i in range(r):
        for j in range(c):
            if graph[i][j]>0: # 미세먼지가 있는 칸
                arc=graph[i][j]//5
                if arc>0:
                    cnt=0
                    for dx,dy in direction:
                        next_x,next_y=dx+i, dy+j
                        if 0<=next_x<r and 0<=next_y<c and graph[next_x][next_y]!=-1:
                            new_graph[next_x][next_y]+=arc
                            cnt+=1
                    new_graph[i][j]-=cnt*arc
    return new_graph

def clean(graph):
    # 위쪽 공기청정기
    # 왼쪽 
    for rr in range(ac[0]-2,-1,-1):
        graph[rr+1][0] = graph[rr][0]
    
    # 위쪽
    for cc in range(1,c):
        graph[0][cc-1]=graph[0][cc]
    
    # 오른쪽
    for rr in range(1,ac[0]+1):
        graph[rr-1][-1]=graph[rr][-1]

    # 아래쪽
    for cc in range(c-2,0,-1):
        graph[ac[0]][cc+1]=graph[ac[0]][cc]
    graph[ac[0]][1]=0

    # 아래쪽 공기청정기
    # 왼쪽
    for rr in range(ac[1]+2,r):
        graph[rr-1][0]=graph[rr][0]

    # 아래쪽
    for cc in range(1,c):
        graph[r-1][cc-1]=graph[r-1][cc]
        
    # 오른쪽
    for rr in range(r-2,ac[1]-1,-1):
        graph[rr+1][-1]=graph[rr][-1]
    
    # 위쪽
    for cc in range(c-2,0,-1):
        graph[ac[1]][cc+1]=graph[ac[1]][cc]
    graph[ac[1]][1]=0

    return graph

for _ in range(t):
    graph=spread(graph)
    graph=clean(graph)
    
answer=0
for i in range(r):
    answer+=sum(graph[i])
print(answer+2)
