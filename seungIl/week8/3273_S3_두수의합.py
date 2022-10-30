# BaekJoon P3273 "두수의 합" (정렬, 투 포인터 | S3)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
주어진 numbers list 를 오름차순으로 정렬한 후
주어진 target 의 중간(mid)지점까지 숫자를 훑으면서
'target - 현재 숫자' 값 이 numbers 에 있는지 판단 -> 있으면 +1

※ mid 까지만 훑는 이유는 mid 를 넘기는 순간 이미 'target - 현재 숫자' 값 으로 인해
이미 search 된 얘이기 때문.
---[비고]---
풀이 시간 : 11m
메모리: 42892 | 시간: 104
"""
import sys


def solution(numbers, x):
    numbers.sort()
    num_set = set(numbers)
    mid = x // 2

    answer = 0
    for n in numbers:
        if n > mid: break
        target = x - n
        if target != n and target in num_set:
            answer += 1

    return answer


if __name__ == '__main__':
    N = int(input())
    inputs = [*map(int, sys.stdin.readline().split())]
    X = int(input())
    print(solution(inputs, X))
