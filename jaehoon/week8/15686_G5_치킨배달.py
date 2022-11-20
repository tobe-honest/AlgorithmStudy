from itertools import combinations
import sys

N,M = map(int,input().split())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

chicken, house, result = [], [], []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])

        elif board[i][j] == 2:
            chicken.append([i, j])

cases = list(combinations(chicken,M))

for case in cases:
    total_distance = 0
    for h in house:
        house_distance = 100
        for i in range(M):
            house_distance = min(house_distance, abs(h[0]-case[i][0])+abs(h[1]-case[i][1]))
        total_distance += house_distance
    result.append(total_distance)
print(min(result))