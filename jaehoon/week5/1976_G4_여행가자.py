
INF = int(1e9)

N = int(input())
M = int(input())

board = []
for i in range(N):
    line = list(map(int,input().split()))
    board.append(line)
    line = []

path = list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if i==j:
            board[i][j] = 0
            continue
        if board[i][j] == 0:
            board[i][j] = INF


for k in range(N):
    for a in range(N):
        for b in range(N):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])
flag=0
start = path[0]-1

for i in range(1,len(path)):
    if board[start][path[i]-1] == INF:
        print("NO")
        flag=1
        break
    start = path[i]-1
    
if flag==0:
    print("YES")