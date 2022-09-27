import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(graph, start):
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))

M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque([])

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))
if not queue:
    print(-1)
    exit()

BFS(graph, queue[0])

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()

print(max([max(i) for i in graph])-1)