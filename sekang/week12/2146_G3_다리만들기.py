from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y):
    return True if 0 <= x < n and 0 <= y < n else False

def numbering_island(i, j, k, gmap, visited):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    gmap[i][j] = k

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(nx, ny) and gmap[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                gmap[nx][ny] = k
                queue.append((nx, ny))
    return gmap, visited

def make_bridge(k, answer):
    dist = [[-1] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if gmap[i][j] == k:
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if check(nx, ny):
                if gmap[nx][ny] > 0 and gmap[nx][ny] != k:
                    return min(answer, dist[x][y])
                
                if not gmap[nx][ny] and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

if __name__ == '__main__':
    n = int(input())
    gmap = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    # Step 1. 섬 구분
    k = 2
    for i in range(n):
        for j in range(n):
            if gmap[i][j] and not visited[i][j]:
                gmap, visited = numbering_island(i, j, k, gmap, visited)
                k += 1
                
    # Step 2. 거리 계산
    answer = 1e9
    for i in range(2, k):
        answer = make_bridge(i, answer)

    print(answer)