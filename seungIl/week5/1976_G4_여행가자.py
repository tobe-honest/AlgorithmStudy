# BaekJoon P1976 "여행가자" (그래프, 자료구조 | G4)
"""
---[실수]---
1. graph를 defalutdict(list)로 만들어서 요소가 중복되는 경우가 있었음 (10분 낭비)
    => defaultdict(set) 으로 중복 요소를 제거해야 됨
    => 혹은 모든 table을 접근하지 말고 우측 상단의 요소들만 접근
    ∴ 항상 만들어진 값들에 대해 출력 해보거나 디버그해서 하나하나 확인 하자
2. visited의 범위를 graph의 len으로 설정 (10분 낭비)
    -> graph에 모든 요소가 들어갈 것이라는 보장이 없음
    ∴ 그냥 주어진 값으로 range 설정하자
---[부족한 점]---
같은 위치가 경로가 될 수 있는 예외 케이스 생각 못함
    -> 1 2 3 뿐만 아니라 1 1 이 경로가 될 수 있음
    => possible 함수에서는 같은 경로에 대해 고려하지 않고 있기 때문에 같은 경로에 대한 처리를 따로 해주어야 함
        if s == e:
            continue
---[풀이]---
먼저 주어진 정보를 통해서 key: parents, value: child 의 dictionary를 생성하고
해당 정보를 이용해서 하나의 경로 (A-B-C 라면 여기서 A-B)에 대한 bfs실행 -> possible(s,e)
possible(s,e) -> dictionary를 통해서 s에서 e까지 갈 수 있는지 판단
---[비고]---
풀이 시간 : 57분
메모리 32440	| 시간: 128
"""
import sys
from collections import defaultdict, deque


def possible(n, start, target, graph):
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    q = deque([start])
    while q:
        curr = q.popleft()
        for ne in graph[curr]:
            if ne == target:
                return True
            if not visited[ne]:
                visited[ne] = 1
                q.append(ne)

    return False


def solution(n, m, table, move):
    graph = defaultdict(set)
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                graph[i + 1].add(j + 1)
                graph[j + 1].add(i + 1)
    for s, e in zip(move, move[1:]):
        if s == e:
            continue
        if not possible(n, s, e, graph):
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    targets = [*map(int, sys.stdin.readline().split())]
    print(solution(N, M, inputs, targets))
