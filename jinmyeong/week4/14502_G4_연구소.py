from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def count(l):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if l[i][j] == 0: cnt += 1
    return cnt

def search(start, graph):
    q = deque([start])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = 2
                q.append((nx, ny))

N, M = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]

zero_l = [(i, j) for i in range(N) for j in range(M) if not l[i][j]]
virus_l = [(i, j) for i in range(N) for j in range(M) if l[i][j] == 2]
candidate = list(combinations(zero_l, 3))
result = -1

for i in range(len(candidate)):
    tmp = copy.deepcopy(l)
    visited = [[False for j in range(M)] for i in range(N)]
    
    for idx, j in enumerate(candidate[i]):
        tmp[j[0]][j[1]] = 1

    for k in range(len(virus_l)):
        x, y = virus_l[k][0], virus_l[k][1]
        if not visited[x][y]:
            search((x, y), tmp)

    c = count(tmp)
    if c > result:
        result = c

print(result)