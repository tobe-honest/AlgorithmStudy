from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(start, graph):
    a = start
    result = 0
    cnt = 0
    size = 2
    while True:
        visited = [[False for j in range(N)] for i in range(N)]
        visited[a[1]][a[2]] = True
        graph[a[1]][a[2]] = 0
        q = deque([a])
        possible = []
        while q:
            d, x, y = q.popleft()
            for i in range(4):
                nd, nx, ny = d + 1, x + dx[i], y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] <= size and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nd, nx, ny))

                    if graph[nx][ny] < size and graph[nx][ny]:
                        possible.append((nd, nx, ny))

        if not possible:
            return result
        possible.sort()

        graph[possible[0][1]][possible[0][2]] = 0
        cnt += 1
        if cnt == size:
            cnt = 0
            size += 1

        result += possible[0][0]
        a = (0, possible[0][1], possible[0][2])


if __name__ == "__main__":
    N = int(input())
    graph = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        if 9 in tmp:
            baby = (0, i, tmp.index(9))
        graph.append(tmp)
    print(dfs(baby, graph))
