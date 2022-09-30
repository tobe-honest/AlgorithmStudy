# BaekJoon P1012 "유기농배추" (그래프, BFS/DFS | S2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
단지 나누기와 똑같은 문제
1이면 거기서 부터 bfs돌려서 땅따먹기 해주고
그 땅따먹기의 시작마다 cnt를 추가해주어 개수를 기록해주면 됨
---[비고]---
풀이 시간 : 18분
메모리 : 32476 | 시간 : 96
"""
import sys
from collections import deque


def bfs(start, graph):
    n, m = len(graph), len(graph[0])
    si, sj = start
    q = deque([[si, sj]])
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    while q:
        ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if graph[ni][nj] == 1:
                    graph[ni][nj] = 0
                    q.append([ni, nj])

    return 1


def solution(m, n, locs):
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for j, i in locs:
        graph[i][j] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                graph[i][j] = 0
                answer += bfs([i, j], graph)

    return answer


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(K)]
        print(solution(M, N, inputs))
