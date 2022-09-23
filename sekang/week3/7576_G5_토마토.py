from collections import deque
import sys
input = sys.stdin.readline

def bfs(tomato, xy, M, N):
    cnt = 0
    Q = deque()
    Q.append([cnt, xy])
    while Q:
        tmp = []
        cnt, xy = Q.popleft()
        for x, y in xy:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < M and 0 <= ny < N and tomato[nx][ny] == 0:
                    tomato[nx][ny] = 1
                    Q.append([cnt + 1, [[nx, ny]]])
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
xy = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            xy.append([i, j])

cnt = bfs(tomato, xy, N, M)

summation = sum([1 if tomato[i][j] == 0 else 0 for i in range(N) for j in range(M)])
print(cnt) if summation == 0 else print(-1)