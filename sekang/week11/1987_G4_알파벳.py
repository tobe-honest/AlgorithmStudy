# 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대 이동 횟수 (시작이 1칸부터)

import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, cnt):
    
    S = set([(x, y, board[0][0])])
    answer = 0

    while S:
        x, y, s = S.pop()
        answer = max(answer, len(s))
    
        if answer >= 26:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in s:
                S.add((nx, ny, s+board[nx][ny]))

    print(answer)
    return

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

bfs(0, 0, 1)