# BaekJoon P2110 "공유기설치" (이진탐색 | G4)
"""
---[실수]---
잘못 접근 -> 거리가 아닌 인덱스에 초점을 맞춤
즉, 이진탐색의 대상이 router 를 설치할 위치(인덱스)가 아닌 최적의 거리가 되어야 함
---[부족한 점]---
이진탐색 문제를 많이 풀어봐야 될 듯!
---[풀이]---
이진탐색의 대상이 router 를 설치할 위치(인덱스)가 아닌 최적의 거리가 되어야 함
그 안에서 최적의 거리가 맞는지 판단하는 조건에 router 가 사용되는 것!
해당 거리로 router 를 설치하니 주어진 개수보다 적은지 큰지를 통해
최적의 거리를 이진탐색으로 구하는 것!
---[비고]---
아직도 result 로 따로 값을 저장한 후에 반환해야 되는 이류를 모르겠음
"""
import sys


def solution(n, c, houses):
    houses.sort()
    min_dis, max_dis = 1, houses[-1] - houses[0] # 최적의 거리후보 최솟값, 최대값
    result = 0
    while min_dis <= max_dis:
        # print(min_dis, max_dis)
        mid = (min_dis + max_dis) // 2 # 최적의 거리 후보
        curr = 0  # 현재 공유기 설치 위치 (defualt : 0th sorted house)
        cnt = 1  # count of router
        # print(mid, '|', houses[curr], end= ' ')
        # 현재 최적의 거리후보로 공유기 설치
        for i in range(n):
            if houses[i] - houses[curr] >= mid:
                curr = i
                cnt += 1
                # print(houses[i], end=' ')
        # print()

        # 현재 최적의 거리후보가 실제 최적의 거리인지 확인 (설치된 공유기의 개수를 통해)
        if cnt >= c : # 후보 변경 -> 최적의 거리가 늘어나야 함 -> 공유기의 개수를 줄이기 위해
            min_dis = mid + 1
            result = mid # ?
        elif cnt < c: # 후보 변경 -> 최적의 거리가 줄어야 함 -> 공유기의 개수를 늘리기 위해
            max_dis = mid - 1

    return result # ?


if __name__ == '__main__':
    N, C = map(int, input().split())
    home_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(solution(N, C, home_list))
