import sys
input=sys.stdin.readline
n,m=map(int,input().split(' '))
graph=list()

for _ in range(n):
    graph.append(list(map(int,input().split(' '))))

global answer
answer=list()
visited=[[False]*m for _ in range(n)]
tetro=[[[0,0],[1,0],[2,0],[3,0]],  #1
        [[0,0],[0,1],[0,2],[0,3]], #2
        [[0,0],[1,0],[0,1],[1,1]], #3
        [[0,0],[0,1],[0,2],[1,1]], #4
        [[0,0],[1,0],[2,0],[1,1]], #5
        [[0,0],[1,0],[1,-1],[2,0]], #6
        [[0,0],[1,0],[1,-1],[1,1]], #7
        [[0,0],[1,0],[2,0],[2,1]], #8
        [[0,0],[1,0],[0,1],[0,2]], #9
        [[0,0],[0,1],[1,1],[2,1]], #10
        [[0,0],[0,1],[0,2],[-1,2]], #11
        [[0,0],[1,0],[2,0],[2,-1]], #12
        [[0,0],[1,0],[1,1],[1,2]], #13
        [[0,0],[1,0],[0,1],[2,0]], #14
        [[0,0],[0,1],[0,2],[1,2]], #15
        [[0,0],[0,1],[-1,1],[-1,2]], #16
        [[0,0],[1,0],[1,1],[2,1]], #17
        [[0,0],[0,1],[1,1],[1,2]], #18
        [[0,0],[1,0],[1,-1],[2,-1]]] #19

def check19(x,y):
    for tet in tetro:
        cnt,flag=0,True
        for t in tet:
            dx,dy=x+t[0],y+t[1]
            if 0<=dx<n and 0<=dy<m:
                cnt+=graph[dx][dy]
            else:
                flag=False
        if flag:
            answer.append(cnt)

for i in range(n):
    for j in range(m):
        check19(i,j)

print(max(answer))