# BaekJoon P9372 "상근이의 여행" (트리, 그래프 이론 | S4)
"""
---[실수]---
---[부족한 점]---
조건을 제대로 보지 못함.
쓸데없는 부가 설명으로 인해 혼란을 겪음
---[풀이]---
현재 이어져있는 그래프의 간선의 개수를 파악하는 방향으로 진행.
근데 결론적으로는 n-1
이상한 문제.
---[비고]---
풀이 시간: 26m
메모리: 34020 | 시간: 276
"""
import sys
from collections import defaultdict, deque


def bfs(start, info, visited):
    q = deque([start])
    used = 0
    while q:
        curr_c = q.popleft()
        for next_c in info[curr_c]:
            if not visited[next_c]:
                used += 1
                visited[next_c] = 1
                q.append(next_c)

    return used


def solution(n, m, airlines):
    info = defaultdict(list)
    for a, b in airlines:
        info[a-1].append(b-1)
        info[b-1].append(a-1)

    visited = [0 for _ in range(n)]
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += bfs(i, info, visited)

    return answer

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(M)]
        print(solution(N, M, inputs))
