
from collections import deque

dI = [-1,1,0,0,0,0]
dJ = [0,0,-1,1,0,0]
dK = [0,0,0,0,-1,1]

def check():
    while queue:
        I,J,K = queue.popleft()
        for i in range(6):
            kI , kJ, kK = I + dI[i] , J + dJ[i], K + dK[i]
            if kI < 0 or kJ < 0 or kK <0 or kI >= H or kJ >= N or kK >= M:
                continue
            
            if board[kI][kJ][kK] == 0:
                board[kI][kJ][kK] = board[I][J][K] + 1
                queue.append([kI,kJ,kK])
                
M,N,H = map(int,input().split())
level = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
board,line = [],[]

for i in range(H):
    line = [list(map(int, input().split())) for _ in range(N)]
    board.append(line)
    line=[]

queue = deque([])

# 익은 토마토 queue에 저장해놓기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                queue.append([i, j, k])

check()

result =  0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result,board[i][j][k])

print(result-1)

# 필요에 따라 solution 함수가 실행되기전queue를 생성하고 데이터를 적절히 저장해놓기
