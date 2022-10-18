# BaekJoon P1447 "휴게소 세우기" (이분탐색 | G4)
"""
---[실수]---
1,2,3,4트 -> 문제 이해 부족
이해를 잘못한 부분
- 휴게소 사이의 거리 측정 시, 고속도로의 처음과 마지막 부분까지 고려해야됨
- 즉, "휴게소가 없는 구간"에
    '고속도로의 시작 ~ 첫 휴게소', '마지막 휴게소 ~ 고속도로의 끝' 도 포함됨
=> points = [0, ... , L] 이 되어야 하는 것
---[부족한 점]---
---[풀이]---
이분 탐색의 대상 : 휴게소 사이의 거리
이분 탐색의 대상 판단 : 해당 거리를 통해 직접 휴게소 설치
 -> 설치 후 개수가 더 많다 => 사이 거리를 늘려 개수 줄이기
 -> 설치 후 개수가 적다 => 사이 거리를 줄여 개수 늘리기
중요한 점 '휴게소가 없는 구간'에 '고속도로의 시작 ~ 첫 휴게소', '마지막 휴게소 ~ 고속도로의 끝'도 포함됨
---[비고]---
풀이 시간: 1h
메모리 : 30840 | 시간 : 68
"""
import sys


# 휴게소 배치
def check(points, distance, n):
    cnt = 0
    for i in range(n + 1):
        curr_point = points[i]
        next_point = points[i + 1]
        while curr_point + distance < next_point:
            cnt += 1
            curr_point += distance

    return cnt


def solution(n, m, l, points):
    points.sort()
    points = [0] + [i for i in points]  # 첫단 처리
    points.append(l)  # 끝단 처리
    start, end = 1, l
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if check(points, mid, n) > m:
            start = mid + 1
        else:
            end = mid - 1
            result = mid

    return result


if __name__ == '__main__':
    N, M, L = map(int, sys.stdin.readline().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(N, M, L, inputs))
