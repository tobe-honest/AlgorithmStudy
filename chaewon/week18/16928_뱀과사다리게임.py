from collections import deque
n,m=list(map(int,input().split(' ')))

snake=dict()
for _ in range(n+m):
    s,e=list(map(int,input().split(' ')))
    snake[s]=e
    
def bfs(x,visited):
    q=deque([x])
    while q:
        x=q.popleft()

        if x==100:
            break
        if x in snake.keys():
            dx=snake[x]
            q.append(dx)
            visited[dx]=visited[x]
        else:
            for i in range(1,7):
                dx=x+i
                if dx<=100 and visited[x]+1<visited[dx]:
                    visited[dx]=visited[x]+1
                    q.append(dx)
    return visited[100]
    
print(bfs(1,[0,0]+[1e9]*99))