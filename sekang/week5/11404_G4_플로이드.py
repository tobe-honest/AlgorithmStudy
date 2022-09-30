def floydwarshall(gmap):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i!=j:
                    gmap[i][j] = min(gmap[i][j], gmap[i][k] + gmap[k][j])
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(gmap[i][j], end=" ") if gmap[i][j] != INF else print(0, end=" ")
        print()

INF = 1e9
N = int(input()) # 도시의 수 2 <= N <= 100
M = int(input()) # 버스의 수 1 <= M <= 100,000
gmap = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split()) # 시작 도시, 도착 도시, 비용
    gmap[a][b] = c if gmap[a][b] == INF else min(gmap[a][b], c)

for i in range(1, N+1):
    gmap[i][i] = 0

floydwarshall(gmap)