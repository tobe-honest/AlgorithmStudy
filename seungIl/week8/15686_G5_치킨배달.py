# BaekJoon P15686 "치킨 배달" (구현, 전수조사, 백트래킹 | G5)
"""
---[실수]---
<<잘못된 접근>>
    bfs로 접근하여 먼저 각 치킨집에 연결된 집의 개수를 파악한 후
    적게 연결된 치킨집을 삭제하는 방식으로 진행
    => 모두 같은 개수의 집이 연결되어있을 경우 해당 접근으로 풀이 불가능
---[부족한 점]---
무조건 bfs 로 접근하는 방식 피하자.
---[풀이]---
각 집과 치킨집의 위치를 기억한 후
주어진 개수에 맞게 조합으로 치킨집 선택
선택 된 치킨집에 따라 각 집의 치킨거리 측정
치킨집 조합 중 총 치킨거리의 최소값 산출
---[비고]---
풀이 시간 : 45m
메모리: 30840 | 시간: 560
"""
import sys
from itertools import combinations

def solution(n, m, graph):
    houses = []
    stores = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                houses.append([i, j])
            elif graph[i][j] == 2:
                stores.append([i, j])

    min_answer = float('inf')
    for case in combinations(stores, m):
        total_dis = 0
        for h in houses:
            min_dis = float('inf')
            for s in case:
                min_dis = min(min_dis, abs(h[0]-s[0])+abs(h[1]-s[1]))
            total_dis += min_dis
        min_answer = min(min_answer, total_dis)

    return min_answer


if __name__ == '__main__':
    N, M = map(int, input().split())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, M, inputs))
