# BaekJoon P1759 "암호만들기" (전수조사, 조합론, 백트래킹 | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
모음 개수에 따른 자음 개수로 모음과 자음 combination 진행
---[비고]---
풀이시간: 11m
메모리: 30840 | 시간: 68
"""
import sys
from itertools import combinations


def solution(l, c, chars):
    m = {'a', 'e', 'i', 'o', 'u'}
    mo = []
    ja = []
    for c in chars:
        if c in m:
            mo.append(c)
        else:
            ja.append(c)

    answer = []
    for mo_cnt in range(1, l-1):
        ja_cnt = l-mo_cnt
        for result_mo in combinations(mo,mo_cnt):
            for result_ja in combinations(ja, ja_cnt):
                temp = result_mo+result_ja
                answer.append(''.join(sorted(temp)))

    return sorted(answer)




if __name__ == '__main__':
    L, C = map(int, input().split())
    inputs = [*sys.stdin.readline().split()]
    print(*solution(L, C, inputs), sep='\n')
