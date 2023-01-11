import sys

sys.setrecursionlimit(10**9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y,x):

    if dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            ky,kx = y+dy[i],x+dx[i] 
            if 0<=kx<n and 0<=ky<n and board[kx][ky] > board[x][y]:
                dp[y][x] = max(dp[y][x],dfs(ky,kx))
    
    return dp[y][x]+1

n = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1 for j in range(n)] for i in range(n)]

ans=0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)