N = int(input())
M = int(input())

INF = int(1e9)

board = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            board[a][b] = 0

for i in range(M):
    a,b,c = map(int,input().split())
    if board[a][b] == 0:
        board[a][b] = c
    elif board[a][b] > c:
        board[a][b] = c

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

for i in range(1,N+1):
    for j in range(1,N+1):
        if board[i][j] == INF:
            print(0,end=' ')
        else:
            print(board[i][j],end=' ')
    print("")