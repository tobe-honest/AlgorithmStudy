# BaekJoon P "" ( | S1)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
모든 지점에 대해서 dfs를 통해 가능한 모든 모형의 합산을 확인하여 최대값을 산출한 뒤
+ 'ㅏㅓㅗㅜ' 에 대해서 합을 파악한 후
최종 최대합 산출
---[비고]---
"""
import sys
from collections import deque


def max_sum(start, graph, n, m):
    global c
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    si, sj = start
    result = 0
    q = deque([[-1, -1, si, sj, 1, graph[si][sj]]])  #
    while q:
        pi, pj, ci, cj, cnt, total = q.popleft()  #
        if cnt == 4:
            result = max(result, total)
            continue
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < n and 0 <= nj < m) and (pi,pj) != (ni,nj):
                c += 1
                q.append([ci, cj, ni, nj, cnt + 1, total + graph[ni][nj]])  #
    return result


def plus_square(center, graph, n, m):
    result = 0
    ci, cj = center
    order = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(4):
        flag = 1
        total = graph[ci][cj]
        for j in range(i, i + 3):
            j = j % 4
            ti, tj = order[j]
            ni, nj = ci + ti, cj + tj
            if 0 <= ni < n and 0 <= nj < m:
                total += graph[ni][nj]
            else:
                flag = 0
                break
        if flag:
            result = max(result, total)

    return result


def solution(n, m, graph):
    answer = 0

    for i in range(n):
        for j in range(m):
            answer = max(answer, max(max_sum([i, j], graph, n, m), plus_square([i, j], graph, n, m)))

    return answer


if __name__ == '__main__':
    c = 0
    N, M = map(int, input().split())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, M, inputs))
    print(c)
