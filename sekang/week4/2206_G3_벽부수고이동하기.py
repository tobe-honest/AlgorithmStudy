import sys
from collections import deque
input = sys.stdin.readline

def bfs(gmap, visited):
    crush = 0
    queue = deque()
    queue.append((crush, 0, 0))
    visited[0][0][crush] = 1
    while queue:
        crush, x, y = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            # for v in visited:
            #     print(v)
            #     print()
            print(visited[x][y][crush])
            return
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] # 상하좌우
            
            if 0 <= nx < N and 0 <= ny < M:
                # 벽 안부수고 이동
                if gmap[nx][ny] == 0 and visited[nx][ny][crush] == 0:
                    queue.append((crush, nx, ny))
                    visited[nx][ny][crush] = visited[x][y][crush] + 1
                # 벽 부수고 이동
                if gmap[nx][ny] == 1 and crush == 0:
                    queue.append((crush + 1, nx, ny))
                    visited[nx][ny][crush + 1] = visited[x][y][crush] + 1
    # for v in visited:
    #     print(v)
    #     print()
    print(-1)
    return

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
gmap = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

bfs(gmap, visited)

# (1,1) -> (N, M) 이동