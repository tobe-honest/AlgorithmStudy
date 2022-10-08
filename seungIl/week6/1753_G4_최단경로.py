# BaekJoon P1753 "최단경로" (그래프, 다익스트라 | G4)
"""
---[실수]---
q에 담는 값의 순서 지정 잘못
-> [비용, 위치] 이렇게 저장해야 되는데 [위치, 비용] 이렇게 저장해버림
-> 우선순위 큐에서 우선순위의 기준이 '비용' 이어야 함!!
---[부족한 점]---
다익스트라를 완벽하게 이해한 상태가 아니였음
if curr_cost > result[curr_loc]: continue 에서 같은 것을 제외하는 이유는
담아놓고 다음 노드로 이동할 때 걸러지게 되기 때문
그럼 같은 것에 대해서도 그냥 search 가 진행 되는 것? -> NO
밑에서 갈 수 있는 다음 노드에 대해 탐색할 때 같은 값은 이미 배제 됨
즉, q에 같은 값이 들어가질 않는 것
---[풀이]---
전형적인 다익스트라 알고리즘
---[비고]---
풀이 시간 : 40m
메모리 : 134336 | 시간 : 1260
"""
import heapq
import sys
from collections import defaultdict


def dja(v, tree, start):
    result = [float('inf') for _ in range(v)]
    result[start] = 0
    q = [[0, start]]
    while q:
        curr_cost, curr_loc = heapq.heappop(q)
        if curr_cost > result[curr_loc]: continue
        for next_loc, next_cost in tree[curr_loc]:
            if next_loc == start: continue
            total_cost = curr_cost + next_cost
            if total_cost < result[next_loc]: # 동일한 값을 여기서 끊어주는 것
                result[next_loc] = total_cost
                heapq.heappush(q, [total_cost, next_loc])
    return result


def solution(v, start, edges):
    tree = defaultdict(list)
    for parent, child, cost in edges:
        tree[parent - 1].append([child - 1, cost])
    result = dja(v, tree, start)
    return [i if i != float('inf') else 'INF' for i in result]


if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    s = int(sys.stdin.readline().strip())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(E)]
    print(*solution(V, s - 1, inputs), sep='\n')
