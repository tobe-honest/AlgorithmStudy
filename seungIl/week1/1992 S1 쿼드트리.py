# BaekJoon P1992 "쿼드트리" (분할정복, 재귀 | S1)
"""
<유형: >
---[실수]---
for i in range(ci, ci + move):
    for j in range(cj, cj + move):
에서 시작점(ci, cj)을 놓침 -> range(ci+move) 이런 식으로 진행해서 실수
---[부족한 점]---
머리 굴리는 게 너무 느림
어떻게 풀어야겠다고 생각은 했는데 이를 구현하기 까지가 오래 걸림
특히 재귀부분이라 그런 듯
---[풀이]---
일반적인 분할정복과 재귀 풀이
근데 중요한 점은 항상 분할 한 후에 반환되는 게 반드시 재귀를 통해 반환되어
결국에는 합쳐지는 형태이어야 한다는 게 중요.
먼저 search 하고자 하는 부분이 모두 일치하지 않는다면 분할 시작
만약 search 하는 부분이 일치하면 정복 시작 -> 조건에 따른 값을 반환하며
정복 시 괄호가 핵심.
    -> 분할 후 정복되어서 합쳐진 것들에 대해선 괄호O
    -> 분할하지 않고 합쳐진 것에 대해선 괄호X
---[비고]---
한번 풀어봤던 문제
"""
import sys

def conquer(gmap, idxes, move):
    ci, cj = idxes
    prev = gmap[ci][cj]
    check = True
    for i in range(ci, ci + move):
        for j in range(cj, cj + move):
            if i == ci and j == cj: continue
            if gmap[i][j] != prev:
                check = False
                break
            prev = gmap[i][j]
        if not check:
            break

    if not check:
        move = move // 2
        temp = '('
        for i in range(2):
            for j in range(2):
                temp += conquer(gmap, [ci + move * i, cj + move * j], move)
        temp += ')'
        return temp
    else:
        return str(prev)


def solution(n, gmap):
    return conquer(gmap, [0, 0], n)


if __name__ == '__main__':
    N = int(input())
    gmap = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    print(solution(N, gmap))
