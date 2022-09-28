# BaekJoon P11404 "플로이드" (그래프, 플로이드-워셜 | G4)
"""
---[실수]---
지점이 0으로 시작하는 것이 아니라 1로 시작하여 인덱스 설정에 문제가 있었음
---[부족한 점]---
플로이드 알고리즘을 사용해보지 않아서 다익스트라로 진행
플로이드 알고리즘 학습 필요
---[풀이]---
다익스트라
플로이드
---[비고]---
풀이 시간: 1h
다익스트라 -> 메모리 : 57380 | 시간 : 2132
플로이드 -> 메모리 : 46980 | 시간 : 408
"""
import heapq
import sys
from collections import defaultdict


# 다익스트라
def dja(s, graph, n):
    temp = [float('inf') for _ in range(n)]
    q = [[0, s]]
    while q:
        cost, curr = heapq.heappop(q)
        if cost > temp[curr]: continue
        for next_loc, next_cost in graph[curr]:
            if next_loc == s: continue  # 시작점으로 되돌아 오는 경우 무시
            total_cost = cost + next_cost
            if total_cost < temp[next_loc]:
                temp[next_loc] = total_cost
                heapq.heappush(q, [total_cost, next_loc])
    result = []
    for t in temp:
        result.append(t if t != float('inf') else 0)

    return result


def for_dja(n, buses):
    graph = defaultdict(list)
    results = []
    # 그래프 생성
    for start, end, cost in buses:
        graph[start - 1].append([end - 1, cost])

    # 각 지점을 시작점으로 설정했을 때의 다익스트라 결과
    for start in range(n):
        results.append(dja(start, graph, n))

    return results


def floyd(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue
                layover = graph[i][k] + graph[k][j]
                if graph[i][j] > layover:
                    graph[i][j] = layover

    return [[graph[i][j] if graph[i][j] != float('inf') else 0 for j in range(n)] for i in range(n)]


def for_floyd(n, buses):
    graph = [[float('inf') for _ in range(n)] for _ in range(n)]
    for start, end, cost in buses:
        if cost < graph[start - 1][end - 1]:
            graph[start - 1][end - 1] = cost
    return floyd(n, graph)


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(M)]
    for f in for_floyd(N, inputs): # or for_dja(N, inputs)
        print(*f)
