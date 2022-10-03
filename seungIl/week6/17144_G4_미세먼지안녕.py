# BaekJoon P17144 "미세먼지안녕" (구현, 시뮬레이션 | G4)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
가장 중요한 포인트는
미세먼지 spread 에서 해당 미세먼지가 퍼지는 순간 바로 해당 값을 적용하여 퍼지게 하는 것이 아니라,
일단 그 값을 다른 graph 에 저장한 후, 다 퍼지고 나서 일괄 적용해야 되는 것이 중요
---[비고]---
풀이 시간 : 50m
메모리 : 30840 | 시간 : 3832
"""
import sys

def spread_mise(c, d, r, room):
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            curr_val = room[i][j]
            if curr_val == -1: continue  # 공기청정기
            if curr_val:  # 미세먼지
                spread_val = curr_val // 5
                spread_cnt = 0
                for di, dj in d:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        if room[ni][nj] == -1: continue  # 공기청정기
                        temp[ni][nj] += spread_val
                        spread_cnt += 1
                room[i][j] = curr_val - spread_val * spread_cnt
    # 퍼진 미세먼지 반영
    for i in range(r):
        for j in range(c):
            room[i][j] += temp[i][j]

def clean_mise(air_clean, c, r, room):
    # 상단
    top = air_clean[0]
    temp = 0
    for j in range(1, c):
        next_temp = room[top][j]
        room[top][j] = temp
        temp = next_temp
    for i in range(top - 1, -1, -1):
        next_temp = room[i][-1]
        room[i][-1] = temp
        temp = next_temp
    for j in range(c - 2, -1, -1):
        next_temp = room[0][j]
        room[0][j] = temp
        temp = next_temp
    for i in range(1, top):
        next_temp = room[i][0]
        room[i][0] = temp
        temp = next_temp
    # 하단
    bottom = air_clean[1]
    temp = 0
    for j in range(1, c):
        next_temp = room[bottom][j]
        room[bottom][j] = temp
        temp = next_temp
    for i in range(bottom + 1, r):
        next_temp = room[i][-1]
        room[i][-1] = temp
        temp = next_temp
    for j in range(c - 2, -1, -1):
        next_temp = room[-1][j]
        room[-1][j] = temp
        temp = next_temp
    for i in range(r - 2, bottom, -1):
        next_temp = room[i][0]
        room[i][0] = temp
        temp = next_temp

def solution(r, c, t, room):
    air_clean = []
    for i in range(r):
        if room[i][0] == -1: air_clean.append(i)
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for _ in range(t):
        # 1. 미세먼지 확산
        spread_mise(c, d, r, room)
        # 2. 공기청정기 작동
        clean_mise(air_clean, c, r, room)

    answer = 0
    for i in range(r):
        for j in range(c):
            mise_value = room[i][j]
            if mise_value != -1:
                answer += mise_value

    return answer

if __name__ == '__main__':
    R, C, T = map(int, input().split())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(R)]
    print(solution(R, C, T, inputs))
