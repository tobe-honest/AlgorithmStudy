from itertools import product
n,m=map(int,input().split(' '))
graph=[]
cctv=[[] for _ in range(7)]

for i in range(n):
    tmp=list(map(int,input().split(' ')))
    for j in range(m):
        if tmp[j]>0:
            cctv[tmp[j]].append([i,j])
    graph.append(tmp)

cases=list()
for i,case in enumerate([list(range(1,5)),list(range(1,3)),list(range(1,5)),list(range(1,5)),[1]]):
    for j in range(len(cctv[i+1])):
        cases.append(case[:])

candidate=list(product(*list(cases)))
def up(graph,x,y):
    for i in range(x-1,-1,-1):
        if graph[i][y]==0:
            graph[i][y]='#'
        elif graph[i][y]==6:
            break
    return graph
def down(graph,x,y):
    for i in range(x+1,n):
        if graph[i][y]==0:
            graph[i][y]='#'
        elif graph[i][y]==6:
            break
    return graph
def right(graph,x,y):
    for i in range(y+1,m):
        if graph[x][i]==0:
            graph[x][i]='#'
        elif graph[x][i]==6:
            break
    return graph
def left(graph,x,y):
    for i in range(y-1,-1,-1):
        if graph[x][i]==0:
            graph[x][i]='#'
        elif graph[x][i]==6:
            break
    return graph
def turn(num,mode,cctv_location,ori_graph):
    graph=[ori[:] for ori in ori_graph]
    x,y=cctv_location[0],cctv_location[1]
    if num==1:
        if mode==1:
            graph=up(graph,x,y)
        elif mode==2:
            graph=down(graph,x,y)
        elif mode==3:
            graph=right(graph,x,y)
        elif mode==4:
            graph==left(graph,x,y)
    elif num==2:
        if mode==1:
            graph=up(graph,x,y)
            graph=down(graph,x,y)
        elif mode==2:
            graph=right(graph,x,y)
            graph==left(graph,x,y)
    elif num==3:
        if mode==1:
            graph=up(graph,x,y)
            graph=right(graph,x,y)
        elif mode==2:
            graph=right(graph,x,y)
            graph=down(graph,x,y)
        elif mode==3:
            graph=down(graph,x,y)
            graph==left(graph,x,y)
        elif mode==4:
            graph==left(graph,x,y)
            graph=up(graph,x,y)
    elif num==4:
        if mode==1:
            graph==left(graph,x,y)
            graph=up(graph,x,y)
            graph=right(graph,x,y)
        elif mode==2:
            graph=up(graph,x,y)
            graph=right(graph,x,y)
            graph=down(graph,x,y)
        elif mode==3:
            graph=right(graph,x,y)
            graph=down(graph,x,y)
            graph==left(graph,x,y)
        elif mode==4:
            graph=down(graph,x,y)
            graph==left(graph,x,y)
            graph=up(graph,x,y)
    elif num==5:
        graph=right(graph,x,y)
        graph=down(graph,x,y)
        graph==left(graph,x,y)
        graph=up(graph,x,y)

    return graph
def count(graph):
    cnt=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                cnt+=1
    return cnt
def observe(cctv,candidate,graph):
    can_idx=0
    for i in range(1,6):
        for j in range(len(cctv[i])):
            graph=turn(i,candidate[can_idx],cctv[i][j],graph) #def turn(num,mode,cctv_location,graph):
            can_idx+=1
    return count(graph)
min_blind=1e9
for can in candidate:
    blind=observe(cctv,can,graph)
    min_blind=blind if blind<min_blind else min_blind
print(min_blind)