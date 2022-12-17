import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y, visited, count):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    count[x][y] += 1

    return visited, count

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    year = 0
    flag = False

    while True:
        visited = [[False] * m for _ in range(n)]
        count = [[0] * m for _ in range(n)]
        length = 0
        
        # 바다 수 확인
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0 and not visited[i][j]:
                    length += 1
                    visited, count = bfs(i, j, visited, count)
        
        # 빙산 크기 줄이기
        for i in range(n):
            for j in range(m):
                graph[i][j] = max(graph[i][j] - count[i][j], 0)

        # 빙산이 다 녹은 경우
        if length == 0:
            break
        
        # 빙산이 분리된 경우
        if length >= 2:
            flag = True
            break

        year += 1

    print(year) if flag else print(0)