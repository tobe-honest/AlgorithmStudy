# BaekJoon P6603 "로또" (수학 | S2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
주어진 번호들에 대한 6가지의 조합을 구하고
해당 조합의 결과들을 정렬
---[비고]---
풀이 시간: 12m
메모리: 30840 | 시간: 68
"""
import sys
from itertools import combinations


def solution(nums):
    answer = []
    for cased in combinations(nums, 6):
        answer.append(cased)
    answer.sort()
    return answer


if __name__ == '__main__':
    while True:
        inputs = [*map(int, sys.stdin.readline().split())]
        if inputs[0] == 0: break
        for ans in solution(inputs[1:]):
            print(*ans)
        print()
