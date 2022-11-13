# BaekJoon P2589 "보물섬" (그래프 | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
L인 모든 지점에 대해서 bfs를 실행하여 가장 먼 곳의 거리를 파악
---[비고]---
문제 이상함. pypy3 를 써야만 통과.
풀이 시간: 15m (첫 제출 시간)
"""
import sys
from collections import deque


def bfs(start, graph, n, m):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    si, sj = start
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[si][sj] = 1
    q = deque([[si, sj, 0]])
    cnt = 0
    while q:
        ci, cj, cnt = q.popleft()
        for di, dj in d:
            ni = ci + di
            nj = cj + dj
            if (0 <= ni < n and 0 <= nj < m) and not visited[ni][nj] and graph[ni][nj] == 'L':
                visited[ni][nj] = 1
                q.append([ni, nj, cnt + 1])

    return cnt


def solution(n, m, graph):
    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                max_dis = bfs([i, j], graph, n, m)
                answer = max(answer, max_dis)

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs = [list(sys.stdin.readline()) for _ in range(N)]
    print(solution(N, M, inputs))
