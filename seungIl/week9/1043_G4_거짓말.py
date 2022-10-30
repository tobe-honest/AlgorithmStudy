# BaekJoon P1043 "거짓말" (그래프, 분리 집합 | G4)
"""
---[실수]---
1,2,3트 : bfs에서 큐에 값을 추가해주는 `q.append(next_n)` 를 빼먹어서 20분 날림 -> 기본인데 실수함
         + `if curr in connections:` 필요 (현재 번호가 connections에 없을 수도 있음)
---[부족한 점]---
이런 작은 한줄을 빼먹거나 이런 실수를 자주하는 듯..
집중 필요. 그리고 내 풀이에 확신이 있는데 틀리면 차근 차근 침착하게 검토하는 침착함이 필요한 듯
---[풀이]---
먼저 모든 파티를 통해
같은 파티에 참여하는 인원들간의 연관관계 생성 후
사실을 알고 있는 인원의 연관관계에 있는 모든 인원들 또한 사실을 알고 있는 사람이라고 치부한 후
각 파티에서 모든 참여자들이 사실을 모르는 파티를 count
---[비고]---
풀이시간: 1h 5m
메모리: 32460 | 시간: 88
"""

import sys
from collections import defaultdict, deque

# 사람들간의 연관관계 생성 (같은 파티에 있을 경우 연관관계 생성)
def make_connections(parties):
    connections = defaultdict(set)
    for party in parties:
        nums = len(party)
        for i in range(nums):
            one = party[i]
            for j in range(i + 1, nums):
                two = party[j]
                connections[one].add(two)
                connections[two].add(one)

    return connections

# 사실을 알고 있는 개인의 전파
def bfs(n, targets, start, connections):
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    q = deque([start])
    while q:
        curr = q.popleft()
        if curr in connections:
            for next_n in connections[curr]:
                if not visited[next_n]:
                    targets.add(next_n)
                    visited[next_n] = 1
                    q.append(next_n)


# 사실을 알고 있는 사람들의 전파 실행 -> 같은 파티에 있을 경우 해당 참여자도 사실을 들어야만 하는 사람
def make_targets(n, facts, connections):
    targets = set(facts)
    for factor in facts:
        bfs(n, targets, factor, connections)
    return targets


def solution(n, m, facts, parties):
    # 사실 전파 실행 -> 사실만을 들어야 하는 사람들을 확인하기 위함
    connections = make_connections(parties)
    # 해당 전파의 결과를 통해 사실만을 들어야 하는 사람들 확인
    targets = make_targets(n, facts, connections)
    # 사실만을 이야기해야 되는 인원이 포함되어 있는 파티 제거
    answer = m
    for party in parties:
        for member in party:
            if member in targets:
                answer -= 1
                break

    return answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs1 = [*map(int, sys.stdin.readline().split())][1:]
    inputs2 = [[*map(int, sys.stdin.readline().split())][1:] for _ in range(M)]
    print(solution(N, M, inputs1, inputs2))