from collections import deque
from itertools import product
from itertools import combinations
from itertools import permutations
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def count_zero(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt+=1
    return cnt

def check(B):
    visited = [[False for i in range(M)] for j in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if B[i][j] == 2:
                queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            kx,ky = x+dx[i], y+dy[i]
            if kx<0 or ky<0 or kx>=N or ky>=M or visited[kx][ky] == True or B[kx][ky] == 1:
                continue
            
            if B[kx][ky] == 0:
                B[kx][ky] = 2
                queue.append([kx,ky])
    return B


N,M = map(int,input().split())

board=[]
for i in range(N):
    lst = list(map(int,input().split()))
    board.append(lst)
    lst = []

nums = []
num = list(range(0, N))
nums.append(num)
num = list(range(0, M))
nums.append(num)

prod = list(product(*nums))
lst = [item for item in prod if board[item[0]][item[1]] == 0]

MAX=0
lst = combinations(lst,3)
for i in lst:
    temp = copy.deepcopy(board)
    temp[i[0][0]][i[0][1]] = 1
    temp[i[1][0]][i[1][1]] = 1
    temp[i[2][0]][i[2][1]] = 1
    c = count_zero(check(temp))
    if c>MAX:
        MAX = c

print(MAX)

