# BaekJoon P1780 "종이의 개수" (분할정복, 재귀 | S2)
"""
<유형: 분할정복, 재귀>
---[실수]---
X
---[부족한 점]---
분할정복을 자주 안풀어보아서 풀이를 생각해 내는데 오래걸림 -> 지능이 딸렸음
---[풀이]---
말 그대로 분할정복과 재귀로 푸는 정석적인 풀이
분할하지 않은 상태에서 조건에 따라 점검을 하고
조건에 맞지 않으면 계속해서 9개로 분할 진행 (재귀)

해당 풀이에서 가장 중요한 부분은 move
move 는 ex) ... -> 9 -> 3 -> 1 의 순으로
가장 처음에는 해당 gmap의 길이를 가지고, 분할이 이루어질 수록 3으로 나뉘어짐
move는 해당 분할된 원소들을 row,col 로 search 하는 길이 제한역할도 하며
분할 시 각각의 시작위치를 지정하는 역할도 함
---[비고]---
6036ms -> 최적화 논의 필요
"""
import sys

def check(gmap, idxes, move):
    # 정해진 범위에서 모든 수가 동일한지 확인 (문제에서 주어진 조건 확인)
    ci, cj = idxes
    prev = gmap[ci][cj]  # 2중 for 문에서 이전 값을 나타내는 변수 (default : 가장 처음 search 하는 원소 값)
    for i in range(ci, ci + move):
        for j in range(cj, cj + move):
            if i == ci and j == cj: continue  # 처음 값은 이전 값이 존재하지 않으므로 pass
            if gmap[i][j] != prev:  # 이전 값과 현재 값이 동일하지 않으면
                return [False, prev]
            prev = gmap[i][j]  # 만약 동일하다면 이전 값을 지금의 값으로 교체 -> 이후에 값이 계속해서 동일한지 확인하기 위함

    return [True, prev]

def conquer(result, gmap, idxes, move):
    ci, cj = idxes # 시작 index
    ch, prev = check(gmap, idxes, move)  # 모든 수가 동일한지 체크하는 변수
    if ch: # 만약 search 한 모든 원소가 동일한 값이다.
        result[prev + 1] += 1 # 해당 수에 맞게 개수 증가
        return
    else: # 만약 동일하지 않다.
        move = move // 3 # 이동 폭을 3으로 줄이고
        # 9개로 다시 분할(각각의 시작 위치 설정)
        for i in range(3):
            for j in range(3):
                conquer(result, gmap, [ci + move * i, cj + move * j], move)


def solution(n, gmap):
    result = [0, 0, 0]
    conquer(result, gmap, [0, 0], n)
    for i in result:
        print(i)


if __name__ == '__main__':
    N = int(input())
    gmap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    solution(N, gmap)
