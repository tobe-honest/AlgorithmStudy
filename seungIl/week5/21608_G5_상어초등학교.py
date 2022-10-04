# BaekJoon P21608 "상어초등학교" (구현 | G5)
"""
---[실수]---
마음이 급해져서 행과 열을 착각
마음이 급해져서 만족도 계산에서 수식을 이상하게 짬 -> info로 값을 가져오는 것이 훨씬 남
---[부족한 점]---
구현 시 급해지면 실수하는 경향이 있음
---[풀이]---
완전 빡구현 그 자체
1. 조건에 따라 학생 앉히기
    - 학생이 앉을 수 있는 모든 자리에 대해서 조건에 따라 계산하여 후보로 지정해주고
    - 자리 후보들 중 조건에 가장 부합(min)한 자리에 현재 학생 배치
2. 완성된 자리에 따른 만족도 계산
    - 각 학생들의 주변 best friends 의 개수를 구하여 만족도 계산 법칙 적용
---[비고]---
메모리 : 30840 | 시간 : 196
"""
import sys


def find_location(graph, n, curr, friends_info):
    candidates = []
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for ci in range(n):
        for cj in range(n):
            friends_cnt = 0
            empty_cnt = 0
            if not graph[ci][cj]:
                for di, dj in d:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        # 1번 조건 (주변 친구 개수)
                        if graph[ni][nj] in friends_info[curr]:
                            friends_cnt += 1
                        # 2번 조건 (주변 빈칸 개수)
                        if graph[ni][nj] == 0:
                            empty_cnt += 1
                candidates.append([-friends_cnt, -empty_cnt, ci, cj])
    _, _, i, j = min(candidates)
    return i, j


def solution(n, students):
    graph = [[0 for _ in range(n)] for _ in range(n)]

    # 조건에 따라 학생 앉히기
    friends_info = dict()
    for st in students:
        friends_info[st[0]] = set(st[1:])
        i, j = find_location(graph, n, st[0], friends_info)
        graph[i][j] = st[0]

    # 만족도 계산
    total = 0
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    score_board = [0,1,10,100,1000]
    for ci in range(n):
        for cj in range(n):
            friends_cnt = 0
            for di, dj in d:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < n:
                    # 1번 조건 (주변 친구 개수)
                    if graph[ni][nj] in friends_info[graph[ci][cj]]:
                        friends_cnt += 1
            total += score_board[friends_cnt]

    return total


if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N * N)]
    print(solution(N, inputs))
