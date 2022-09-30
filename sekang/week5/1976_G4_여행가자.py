import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
def search(gmap, load):
    # 사전 준비
    for i in range(N):
        for j in range(N):
            if gmap[i][j] == 0 and i != j:
                gmap[i][j] = INF

    # 플로이드와샬
    for k in range(N):
        for i in range(N):
            for j in range(N):
                gmap[i][j] = min(gmap[i][j], gmap[i][k] + gmap[k][j])
    # print(gmap)

    flag = True
    # 연결 여부 확인
    for i in range(1, M):
        start, end = load[i-1], load[i] # 1 ~ M - 1
        if gmap[start][end] == INF: # 길 x
            flag = False
            break

    print('YES') if flag else print('NO')
    return
    

N = int(input()) # 도시의 수(N <= 200)
M = int(input()) # 여행 계획에 속한 도시의 수(M <= 1000)
gmap = [list(map(int, input().split())) for _ in range(N)] # N x N
load = list(map(int, input().split())) # 1 x M
for i in range(M):
    load[i] -= 1
search(gmap, load)