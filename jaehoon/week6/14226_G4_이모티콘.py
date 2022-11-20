from collections import deque

def bfs():
    queue = deque([[0,1,0]])
    visit = [[False for i in range(1001)] for j in range(1001)]

    while queue:
        x,y,t = queue.popleft()
        visit[x][y] = True

        if S==y:
            return t

        if 0 <= y <= 1000 and visit[y][y]==False:
            queue.append([y,y,t+1])
            visit[y][y] = True

        if 0<= x <= 1000 and 0<= y+x <=1000 and visit[x][y+x] == False:
            queue.append([x,y+x,t+1])
            visit[x][x+y] = True
        
        if 0<= x <= 1000 and 0<= y-1 <=1000 and visit[x][y-1]==False:
            queue.append([x,y-1,t+1])
            visit[x][y-1] = True

S = int(input())
print(bfs())