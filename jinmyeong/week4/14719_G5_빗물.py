from collections import deque
input= __import__("sys").stdin.readline

def check(x, y):
    if 0 <= x < H and 0 <= y < W:
        return True
    return False

def search(start, graph):
    visited = [[False for j in range(W)] for i in range(H)]
    visited[start[0]][start[1]] = True
    q = deque([start])
    while q:
        x, y = q.popleft()
        
        if check(x-1, y) and check(x-1,y-1) and check(x-1, y+1) and graph[x-1][y] == 0 and (graph[x-1][y-1]==1 or graph[x-1][y+1]==1):
            visited[x-1][y] = True
            q.append((x-1, y))
            graph[x-1][y] = 2

        if check(x+1, y) and check(x+1, y-1) and check(x+1, y+1) and graph[x+1][y] == 0 and (graph[x+1][y-1]==1 or graph[x+1][y+1]==1):
            visited[x+1][y] = True
            q.append((x+1, y))
            graph[x+1][y] = 2

        if check(x, y-1) and check(x, y-2) and check(x, y) and graph[x][y-1] == 0 and (graph[x][y-2]==1 or graph[x][y]==1):
            visited[x][y-1] = True
            q.append((x, y-1))
            graph[x][y-1] = 2
        if check(x, y+1) and check(x, y) and check(x, y+2) and graph[x][y+1] == 0 and (graph[x][y]==1 or graph[x][y+2]==1):
            visited[x][y+1] = True
            q.append((x, y+1))
            graph[x][y+1] = 2

        
H, W = map(int, input().split())
l = list(map(int, input().split()))
graph = [[0 for j in range(W)] for i in range(H)]
for idx, val in enumerate(l):
    for i in range(H-val, H):
        graph[i][idx] = 1

s_l = [(i,j) for i in range(H) for j in range(W)]
s_l = []
for i in range(H):
    for j in range(1,W):
        if check(i-1, j) and check(i, j-1) and check(i, j+1) and (graph[i-1][j] == 1 or graph[i][j-1] == 1 or graph[i][j+1] == 1):
            search((i, j), graph)
# for i in range(H):
    # for j in range(W):
        # if not graph[i][j-1]: graph[i][j] = 0


print(graph)


