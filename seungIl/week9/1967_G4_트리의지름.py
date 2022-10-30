# BaekJoon P1967 "트리의지름" (그래프 | G4)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
먼저, 루트에서 가장 멀리 있는 노드를 측정한 후
해당 노드에서 가장 멀리 있는 노드까지의 길이 측정
---[비고]---
풀이 시간 : 2h
메모리: 46992 | 시간: 120
"""

import sys
from collections import defaultdict
sys.setrecursionlimit(100000)


def dfs(prev, curr, info, max_info, total_cost):
    for next_node, next_cost in info[curr]:
        if next_node == prev: continue
        dfs(curr, next_node, info, max_info, total_cost + next_cost)

    max_node, max_cost = max_info
    if max_cost < total_cost:
        max_info[0] = curr
        max_info[1] = total_cost


def solution(edges):
    info = defaultdict(list)
    for a, b, cost in edges:
        info[a].append([b, cost])
        info[b].append([a, cost])

    max_info = [0, 0] # 가장 먼 노드, 그 길이
    # 루트에서 가장 먼 노드
    dfs(0, 1, info, max_info, 0)
    # 가장 먼 노드에서 가장 먼 노드 -> 지름
    dfs(0, max_info[0], info, max_info, 0)
    return max_info[1]

if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N - 1)]
    print(solution(inputs))
