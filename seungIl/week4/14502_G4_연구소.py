# BaekJoon P14502 "연구소" ( 그래프, 전수조사 | G4)
"""
---[실수]---
---[부족한 점]---
전수조사로 풀면 무조건 안될 것이라 생각함 -> 분명 시간초과가 발생할 것이라고 생각
---[풀이]---
가장 먼저 벽이 될 수 있는 후보(0)들과 바이러스(2)의 위치를 확인한 후
전수조사(조합->combinations)를 통해 안전구역의 크기가 가장 큰 놈을 확인
이때 각 후보들의 조합을 통해 일일히 해당 조합으로 인해 벽이 설치 될 때의 바이러스의 전파(bfs) 후 안전구연의 크기 확인
---[비고]---
1트 -> 메모리 : 32516 | 시간 : 3440 (deepcopy 사용)
2트 -> 메모리 : 32500 | 시간 : 2412 (list comprehension)
추가적으로 시간을 줄일 방법은 있을 듯
"""
import sys
from collections import deque
from itertools import combinations


def bfs(wmap, viruses, n, m):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque(viruses)
    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < n and 0 <= nj < m) and wmap[ni][nj] == 0:
                wmap[ni][nj] = 2
                q.append([ni, nj])


def solution(n, m, graph):
    candidates = [] # 새로운 3개의 벽 후보 (위치)
    viruses = [] # 바이러스의 위치
    # 벽 후보와 바이러스 위치 확인
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                candidates.append([i, j])
            elif graph[i][j] == 2:
                viruses.append([i, j])

    max_result = 0 # 결과 값
    # 벽 후보에 대한 조합 확인 (전수 조사)
    for walls in combinations(candidates, 3):
        wmap = [[graph[i][j] for j in range(m)] for i in range(n)] # list comprehension
        for wi, wj in walls: # 벽 설치
            wmap[wi][wj] = 1
        bfs(wmap, viruses, n, m) # 해당 벽에 따른 바이러스 전파
        result = 0
        # 안전구역 확인
        for k in range(n):
            result += wmap[k].count(0)
        max_result = max(max_result, result) # 지속적으로 값 비교

    return max_result


if __name__ == '__main__':
    N, M = map(int, input().split())
    gmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, M, gmap))
