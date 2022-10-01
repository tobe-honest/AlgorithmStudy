from collections import deque
input=__import__("sys").stdin.readline 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check(x, y):
    return 0 <= x < M and 0 <= y < N
def BFS(graph, start):
    queue = deque([start])
    a, b = start
    graph[a][b] = 0

    while queue:
        y, x = queue.popleft()
        
        if check(x, y-1):
            if graph[y-1][x] == 1:
                graph[y-1][x] = 0
                queue.append((y-1, x))
        if check(x, y+1):
            if graph[y+1][x] == 1:
                graph[y+1][x] = 0
                queue.append((y+1, x))
        if check(x-1, y):
            if graph[y][x-1] == 1:
                graph[y][x-1] = 0
                queue.append((y, x-1))
        if check(x+1, y):
            if graph[y][x+1] == 1:
                graph[y][x+1] = 0
                queue.append((y, x+1))
        # for i in range(4):
        #     nx = x + dx[i]
        #     ny = y + dy[i]

        #     if nx < 0 or ny < 0 or nx >= M or ny >= N:
        #         continue
        #     if graph[ny][nx] == 1:
        #         graph[ny][nx] = 0
        #         queue.append((ny, nx))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        cnt = 0
        M, N, K = map(int, input().split())
        graph = [[0]*M for i in range(N)]
        
        for __ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1:
                    BFS(graph, (y, x))
                    cnt += 1
        print(cnt)