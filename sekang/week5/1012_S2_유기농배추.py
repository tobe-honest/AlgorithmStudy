import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(gmap, x, y):
    if 0 > x or x >= M or 0 > y or y >= N:
        return False
    if gmap[x][y] == 1:
        gmap[x][y] = 0
        dfs(gmap, x-1, y)
        dfs(gmap, x+1, y)
        dfs(gmap, x, y-1)
        dfs(gmap, x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(K)]
    cnt = 0

    # visited = [[False] * N for _ in range(M)]
    gmap = [[0] * N for _ in range(M)]
    for x, y in info:
        gmap[x][y] = 1

    for i in range(M):
        for j in range(N):
            if dfs(gmap, i, j):
                cnt += 1
    print(cnt)