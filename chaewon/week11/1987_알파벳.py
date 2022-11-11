from collections import deque
r,c=map(int,input().split(' '))
graph=[]
for _ in range(r):
    graph.append(input())

direc=[[1,0,0,-1],[0,1,-1,0]]
q=set([(0,0,graph[0][0])])
block=1
while q:
    x,y,alpha=q.pop()
    if block>=26:
        break
    for i in range(4):
        dx,dy=x+direc[0][i],y+direc[1][i]
        if 0<=dx<r and 0<=dy<c and graph[dx][dy] not in alpha:
            q.add((dx,dy,alpha+graph[dx][dy]))
            block=max(block,len(alpha)+1)

print(block)