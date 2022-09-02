from collections import deque
n=int(input())
dx=[-2,-2,-1,1,2,2,1,-1]
dy=[-1,1,2,2,1,-1,-2,-2]

def bfs(visited,start_x,start_y,end_x, end_y):
    q=deque([(start_x,start_y)])
    
    while q:
        x,y=q.popleft()
        
        if x==end_x and y==end_y:
            break
        
        for dxx,dyy in zip(dx,dy):
            next_x=x+dxx
            next_y=y+dyy
            if next_x<i and next_x>=0 and next_y<i and next_y>=0:
                if visited[next_x][next_y]==0:
                    q.append((next_x,next_y))
                    visited[next_x][next_y]=visited[x][y]+1
    
    print(visited[end_x][end_y])



for _ in range(n):
    i=int(input())
    start_x, start_y=map(int,input().split(' '))
    end_x, end_y=map(int,input().split(' '))

    visited=[[0 for _ in range(i)] for __ in range(i)]
    bfs(visited,start_x,start_y,end_x, end_y)
    
