from collections import deque
import copy
def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited = [[0] * N for _ in range(N)]
    dist = copy.deepcopy(visited)
    eat = []
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft() # 현 위치(i, j와 다름)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if shark[nx][ny] <= shark[i][j] or shark[nx][ny] == 0: # 이동 가능한 경우
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                if shark[nx][ny] < shark[i][j] and shark[nx][ny] != 0: # 먹을 수 있는 경우 (일단 저장)
                    eat.append([nx, ny, dist[nx][ny]])
    if not eat: return -1, -1, -1
    eat.sort(key = lambda x : (x[2], x[0], x[1])) # 거리-x-y 기준 정렬 (오름차순)
    return eat[0][0], eat[0][1], eat[0][2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
shark = [list(map(int, input().split())) for _ in range(N)]
x = sum([i if shark[i][j] == 9 else 0 for i in range(N) for j in range(N)])
y = sum([j if shark[x][j] == 9 else 0 for j in range(N)])
shark[x][y] = 2
ate = 0
cnt = 0
while True:
    i, j = x, y
    ex, ey, dist = bfs(i, j) # 먹을 수 있는 물고기 찾기 (다음 위치 + 거리 반환)
    if ex == -1: break
    shark[ex][ey], shark[i][j] = shark[i][j], 0
    x, y = ex, ey
    ate += 1
    if ate == shark[ex][ey]:
        ate = 0
        shark[ex][ey] += 1
    cnt += dist

print(cnt)