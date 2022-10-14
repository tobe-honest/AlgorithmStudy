# BaekJoon P2217 "로프" (그리디 | S4)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
먼저 주어진 로프들을 내림차순으로 정렬하고
순서에 맞게 결과 값을 비교하며 최대 값 산출

내림차순 정렬 -> 최대값을 산출해 내기 위해서 큰 순서대로 선택해야 됨
idx * val -> 현재 고른 로프들을 통해 들 수 있는 최대 무게
 - 이전 로프들에 대해 판단하지 않는 이유 => 이전 값은 어차피 현재 값보다 크기에 고려하지 않아도 됨
 - (인덱스+1)에 해당 값을 곱하는 이유 => 로프의 개수를 선택할 때, 선택한 로프의 가장 적은 값을 가진 로프 * 개수 가 현재 최대로 들 수 있는 무게 이므로
 ex) [12,9,3] -> 1: 12*1=12, 2: 9*2=18, 3: 3*3=9
---[비고]---
풀이 시간 : 11m
메모리 : 33668 | 시간 : 148
"""
import sys


def solution(ropes):
    ropes.sort(reverse=True)
    max_result = 0
    for idx, val in enumerate(ropes,1):
        max_result = max(max_result, val*idx)
    return max_result


if __name__ == '__main__':
    N = int(input())
    inputs = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(solution(inputs))