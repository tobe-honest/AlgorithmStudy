import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]

dp = [[(99999999, -1) for i in range(M+2)] for i in range(N)]
for i in range(1, M+1):
    dp[0][i] = (l[0][i-1], -1)

# print(dp)
for i in range(1, M+1):
    a, b = min(dp[0][i-1], min(dp[0][i], dp[0][i+1]))
    if a == dp[0][i+1][0]: b = 1
    if a == dp[0][i][0]: b = 2
    if a == dp[0][i-1][0]: b = 3
    dp[1][i] = (a + l[1][i-1], b)

for i in range(2, N):
    for j in range(1, M+1):
        if dp[i-1][j-1][1] == 3 or dp[i-1][j-1][1] == -1:
            a, b = min(dp[i-1][j], dp[i-1][j+1])
            b = 2 if a == dp[i-1][j][0] else 1
            dp[i][j] = (a + l[i][j-1], b)
        if dp[i-1][j][1] == 2 or dp[i-1][j][1] == -1:
            a, b = min(dp[i-1][j-1], dp[i-1][j+1])
            b = 3 if a == dp[i-1][j-1][0] else 1
            dp[i][j] = (a + l[i][j-1], b)
        if dp[i-1][j+1][1] == 1 or dp[i-1][j+1][1] == -1:
            a, b = min(dp[i-1][j-1], dp[i-1][j])
            b = 3 if a == dp[i-1][j-1][0] else 2
            dp[i][j] = (a + l[i][j-1], b)
print(dp)
# print(min(dp[-1])[0])
        # dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i-1][j+1])) + l[i-1][j-1]