from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(gmap, virus):
    global res
    virus2 = deepcopy(virus)
    visited = [[False] * M for _ in range(N)]
    while virus2:
        x, y = virus2.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if gmap[nx][ny] == 0:
                    visited[nx][ny] = True
                    virus2.append((nx, ny))
        
    res = sum([1 if gmap[i][j] == 0 and not visited[i][j] else 0 for i in range(N) for j in range(M)])
    return res

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
gmap = []
safe = []
res = 0
virus = deque()

N, M = map(int, input().split())
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(M):
        if lst[j] == 2:
            virus.append((i, j))
        if lst[j] == 0:
            safe.append((i, j))
    gmap.append(lst)

for a, b, c in combinations(safe, 3):
    gmap[a[0]][a[1]] = gmap[b[0]][b[1]] = gmap[c[0]][c[1]] = 1
    res = max(res, bfs(gmap, virus))
    gmap[a[0]][a[1]] = gmap[b[0]][b[1]] = gmap[c[0]][c[1]] = 0

print(res)