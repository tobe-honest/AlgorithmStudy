from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search(start, board, visited):
    q = deque([start])
    visited[start[0]][start[1]] = True
    board[start[0]][start[1]] = '0'
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and int(board[nr][nc]):
                visited[nr][nc] = True
                board[nr][nc] = '0'
                q.append((nr, nc))
                cnt += 1
    return cnt

N = int(input())
board = [list(input().strip()) for i in range(N)]
visited = [[False for j in range(N)] for i in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
           result.append(search((i, j), board, visited))
result.sort()
print(len(result))
for i in result:
    print(i)