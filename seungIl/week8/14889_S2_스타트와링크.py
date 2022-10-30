# BaekJoon P14889 "스타트와 링크" (전수조사, 백트래킹 | S2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
<<전수조사>>
조합(combinations 사용)을 통해 먼저 하나의 팀을 완성한 후
해당 팀에 속하지 않는 나머지 사람들로 남은 팀 완성
그리고 주어진 graph 를 통해 각 팀의 점수 계산 및 점수 차 측정
각 조합에서 주어진 팀과 나머지 팀의 점수 차 중 가장 작은 점수를 반환
---[비고]---
풀이시간 : 18m
메모리: 30840 | 시간: 3296
시간이 120 나오는 Best Code 궁금함
이게 왜 백트래킹?
"""
import sys
from itertools import combinations


def solution(n, infos):
    diff = float('inf')
    for team_a in combinations(range(n),n//2):
        result_a = result_b = 0
        check_a = set(team_a)
        team_b = []
        for i in range(n):
            if i not in check_a:
                team_b.append(i)
        for a1 in team_a:
            for a2 in team_a:
                result_a += infos[a1][a2]
        for b1 in team_b:
            for b2 in team_b:
                result_b += infos[b1][b2]
        diff = min(diff, abs(result_a - result_b))

    return diff


if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N,inputs))