from collections import deque

t = int(input())

def bfs(start_x, start_y, end_x, end_y):
    queue = deque()
    queue.append((start_x, start_y))
    
    while queue:
        x, y = queue.popleft()
        
        # 성공 조건
        len_x, len_y = abs(x - end_x), abs(y - end_y)

        # 도착 조건
        if len_x + len_y <= 1000:
            print('happy')
            return

        # 탐색
        for i in range(n):
            len_x, len_y = abs(x - dist[i][0]), abs(y - dist[i][1])
            if  len_x + len_y <= 1000 and not visited[i]:
                queue.append((dist[i][0], dist[i][1]))
                visited[i] = True

    print('sad')
    return


for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    dist = [list(map(int, input().split())) for _ in range(n)]

    end_x, end_y = map(int, input().split())
    
    visited = [False] * n
    bfs(start_x, start_y, end_x, end_y)