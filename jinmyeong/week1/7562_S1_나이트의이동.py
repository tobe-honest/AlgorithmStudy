from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

def search(now, board, l):
    q = deque([now])
    board[now[0]][now[1]] = 1
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < l and 0 <= nc < l and not board[nr][nc]:
                q.append([nr, nc])
                board[nr][nc] = board[r][c] + 1

            if [nr, nc] == target:
                print(board[nr][nc]-1)
                return
        
T = int(input())
for _ in range(T):
    cnt = 0
    l = int(input())
    start, target = list(map(int, input().split())), list(map(int, input().split()))
    board = [[0 for j in range(l)] for i in range(l)]
    search(start, board, l)