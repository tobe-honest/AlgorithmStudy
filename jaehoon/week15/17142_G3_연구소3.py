from collections import deque
from itertools import combinations
import sys

inf = sys.maxsize
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(active):
    queue = deque()
    visited = [[-1 for j in range(n)] for i in range(n)]
    result = 0

    for y, x in active:
        queue.append((y, x))
        visited[y][x] = 0

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            ky, kx = y + dy[i], x + dx[i]

            if 0 <= ky < n and 0 <= kx < n:
                if graph[ky][kx] == 0 and visited[ky][kx] == -1:
                    queue.append((ky, kx))
                    visited[ky][kx] = visited[y][x] + 1
                    result = max(result, visited[ky][kx])

                elif graph[ky][kx] == 2 and visited[ky][kx] == -1:
                    queue.append((ky, kx))
                    visited[ky][kx] = visited[y][x] + 1

    if list(sum(visited, [])).count(-1) != cnt:
        return inf
    else:
        return result




n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1 # 벽의 개수
        elif graph[i][j] == 2:
            virus.append((i, j))

ans = inf
for active in combinations(virus, m):
    ans = min(ans, bfs(active))

print(ans if ans != inf else -1)

