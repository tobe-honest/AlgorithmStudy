from collections import deque
import sys
input = sys.stdin.readline

# bfs 함수 정의
def bfs(cnt, x, y):
    queue = deque()
    queue.append((cnt, x, y))

    while queue:
        cnt, x, y = queue.popleft()

        # 도착 지점에 도달하면 종료
        if x==end_x and y == end_y:
            return cnt

        # 나이트가 이동 가능한 8방향 전부 수행
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 최소 거리를 구해야 하기 때문에 방문 안한 지점만 방문
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((cnt+1, nx, ny))

n = int(input())

cnt = []
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

# 입력 및 함수 호출
for _ in range(n):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    visited = [[False] * l for _ in range(l)]

    cnt.append(bfs(0, start_x, start_y))

# 출력
for i in range(n):
    print(cnt[i])