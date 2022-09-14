# BaekJoon P13397 "구간나누기2" (이분탐색 | G4)
"""
---[실수]---
---[부족한 점]---
이분탐색 어려워~
항상 이분탐색의 대상을 누구로 정하고
해당 대상이 최적의 값인지를 판단을 어떻게 할것인지를 잘 정하는 것이 중요
---[풀이]---
이분탐색의 대상 : 한 구간의 최대 최소 값의 차
이분탐색의 대상이 최적의 값인지 판단 -> 해당 값으로 구간을 나누었을 때의 결과 값과 m을 비교

한 구간의 최대 최소 값의 차(mid(==diff))가
    작을 수록 -> 한 구간에 들어갈 수 있는 요소들의 개수는 줄어들고 -> 총 구간의 개수(m)는 늘어남
    클 수록 -> 한 구간에 들어갈 수 있는 요소들의 개수는 늘어나고 -> 총 구간의 개수(m)는 줄어듦
따라서 check을 통해서 나온 총 구간의 개수(cnt)가 주어진 m 보다
    작거나 같으면 -> 찾고자하는 값(diff)을 줄여서 총 구간의 개수를 키워야되는 것
    크면 -> 찾고자하는 값(diff)을 더 키워 총 구간의 개수를 줄여야되는 것
---[비고]---
메모리 : 30852 | 시간 : 100
if cnt == m : return mid 는 왜 안되는가?
cnt랑 m이랑 같은 순간의 mid를 바로 반환하면 되지않나?
"""
import sys


# 주어진 diff 로 몇개의 구간을 생성해내는 지 확인
def check(n, li, diff):
    print(diff)
    cnt = 1
    idx = 0
    part_max = li[0]
    part_min = li[0]

    while True:
        print(idx, '|', part_max, part_min,'|',cnt)
        # 구간 이어나가기
        if part_max - part_min <= diff:
            idx += 1
            if idx >= n: break
            part_max = max(part_max, li[idx])
            part_min = min(part_min, li[idx])
        # 구간 끊기
        else:
            cnt += 1
            part_max = li[idx]
            part_min = li[idx]
    return cnt


def solution(n, m, li):
    end = max(li) - min(li)
    start = 0
    result = 0
    # 이분탐색 (대상 : 한 구간의 최대 최소값의 차이)
    while start <= end:
        mid = (start + end) // 2
        # 주어진 diff 로 몇개의 구간을 생성해내는 지 확인
        if check(n,li, mid) <= m: # 적거나 같다 -> 찾고자하는 값(diff)을 줄여서 총 구간의 개수를 늘려야 됨
            end = mid - 1
            result = mid # ?
        else: # 많다 -> 찾고자하는 값(diff)을 더 키워 총 구간의 개수를 줄여야되는 것
            start = mid + 1

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    li = list(map(int, sys.stdin.readline().split()))
    print(solution(N, M, li))
