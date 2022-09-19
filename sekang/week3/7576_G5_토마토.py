from collections import deque
import sys
input = sys.stdin.readline

def bfs(tomato, i, j, M, N):
    cnt = 0
    Q = deque()
    Q.append([cnt, i, j])
    
    while Q:
        cnt, x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                Q.append([cnt + 1, nx, ny])
        print(cnt)
    return cnt

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
total = [0]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            total.append(bfs(tomato, i, j, N, M))

summation = sum([1 if tomato[i][j] == 0 else 0 for i in range(N) for j in range(M)])
print(max(total)) if summation == 0 else print(-1)

# 1이 들어있는게 여러개 있을 수 있으니까 한번에 해야하네? -> 같이 시작
# bfs cnt는 안에 넣는게 맞는 듯 (몇번 횟수를 실행했는지 찾을 때)
# summation 쓸거면 연습하기