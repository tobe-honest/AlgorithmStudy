# BaekJoon P12100 "2048(Easy)" (구현, 시뮬레이션 | G2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
전수 조사 -> 4가지 방향에 대해 최대 5번의 모든 경우를 시뮬레이션을 돌려 최대값 확인
dfs를 통해 전수 조사를 진행했으며,
각 dfs에서의 방향에 따른 움직임과 병합 과정은 compose를 통해 구현
compose()
    - 일단 정해진 방향에 따라 움직이며 병합함
    - 방향의 종착지점에서 시작지점으로 순서를 정하여
    - 현재 focuse 되어 있는 값을 가능한 종착지점까지 옮김
    - 옮긴 후 해당 값이 병합이 되면 병합 실시
    - 하지만 이미 병합된 놈이면 병합 X -> composed를 통해 구분
---[비고]---
풀이 시간 : 54m
메모리: 30840 | 시간: 544
"""
import sys

# 정해진 방향에 따른 움직임 + 병합 과정
def compose(n, curr_d, temp):
    if curr_d == 0:
        for i in range(n):
            composed = [0 for _ in range(n)]
            for j in range(n - 2, -1, -1):
                if temp[i][j] == 0: continue
                cj = j
                nj = j + 1
                while nj < n and temp[i][nj] == 0:
                    t = temp[i][cj]
                    temp[i][cj] = 0
                    temp[i][nj] = t
                    cj += 1
                    nj += 1
                if nj < n:
                    if temp[i][cj] == temp[i][nj] and composed[cj]+composed[nj] == 0:
                        temp[i][nj] += temp[i][cj]
                        temp[i][cj] = 0
                        composed[nj] = 1

    if curr_d == 1:
        for i in range(n):
            composed = [0 for _ in range(n)]
            for j in range(1, n):
                if temp[i][j] == 0: continue
                cj = j
                nj = j - 1
                while nj >= 0 and temp[i][nj] == 0:
                    t = temp[i][cj]
                    temp[i][cj] = 0
                    temp[i][nj] = t
                    cj -= 1
                    nj -= 1
                if nj >= 0:
                    if temp[i][cj] == temp[i][nj] and composed[cj]+composed[nj] == 0:
                        temp[i][nj] += temp[i][cj]
                        temp[i][cj] = 0
                        composed[nj] = 1

    if curr_d == 2:
        for j in range(n):
            composed = [0 for _ in range(n)]
            for i in range(1,n):
                if temp[i][j] == 0: continue
                ci = i
                ni = i - 1
                while ni >= 0 and temp[ni][j] == 0:
                    t = temp[ci][j]
                    temp[ci][j] = 0
                    temp[ni][j] = t
                    ci -= 1
                    ni -= 1
                if ni >= 0:
                    if temp[ci][j] == temp[ni][j] and composed[ci] + composed[ni] == 0:
                        temp[ni][j] += temp[ci][j]
                        temp[ci][j] = 0
                        composed[ni] = 1

    if curr_d == 3:
        for j in range(n):
            composed = [0 for _ in range(n)]
            for i in range(n - 2, -1, -1):
                if temp[i][j] == 0: continue
                ci = i
                ni = i + 1
                while ni < n and temp[ni][j] == 0:
                    t = temp[ci][j]
                    temp[ci][j] = 0
                    temp[ni][j] = t
                    ci += 1
                    ni += 1
                if ni < n:
                    if temp[ci][j] == temp[ni][j] and composed[ci] + composed[ni] == 0:
                        temp[ni][j] += temp[ci][j]
                        temp[ci][j] = 0
                        composed[ni] = 1

# 해당 맵에서 가장 큰 값 산출
def find_max(n, graph):
    max_val = 0
    for i in range(n):
        for j in range(n):
            max_val = max(max_val, graph[i][j])
    return max_val

# 4가지 모든 방향에 대한 최대 5가지 순열
def dfs(n, curr_d, graph, cnt):
    temp = [[graph[i][j] for j in range(n)] for i in range(n)]
    compose(n, curr_d, temp)
    max_val = find_max(n, temp)

    if cnt == 5:
        return max_val

    for next_d in range(4):
        max_val = max(max_val, dfs(n, next_d, temp, cnt+1))
    return max_val


def solution(n, graph):
    max_val = find_max(n, graph)
    for curr_d in range(4):
        max_val = max(max_val, dfs(n, curr_d, graph, 1))

    return max_val

if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, inputs))
