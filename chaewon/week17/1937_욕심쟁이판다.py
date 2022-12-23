import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
graph=list()
for i in range(n):
    graph.append(list(map(int,input().split(' '))))
direction=[[-1,1,0,0],[0,0,-1,1]]
answer=[[0]*n for _ in range(n)]
def dfs(x,y):
    if answer[x][y]>0:
        return answer[x][y]
    answer[x][y]=1
    for i in range(4):
        dx,dy=x+direction[0][i],y+direction[1][i]
        if 0<=dx<n and 0<=dy<n and graph[dx][dy]>graph[x][y]:
            answer[x][y]=max(dfs(dx,dy)+1, answer[x][y])
    return answer[x][y]

result=0
for i in range(n):
    for j in range(n):
        result=max(result,dfs(i,j))
print(result)