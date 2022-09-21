# BaekJoon P1374 "강의실" (자료구조,그리디,정렬,우선순위큐 | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
먼저 시작순으로 정렬해주고
정렬된 순으로 강의를 훑으면서
현재 접근한 강의가 가장 빨리 끝나는 강의가 끝나기 전에 시작하면 새로운 강의실 배치 (+1)
현재 접근한 강의가 가장 빨리 끝나는 강의가 끝난 후에 시작하면 해당 강의실을 현재 접근한 강의실에 배치 (+0)
그때 가장 빨리 끝나는 강의를 우선순위큐(heapq)를 사용해서 확인
% 하나씩 접근하기 때문에 하나씩 강의실을 교환해도 되는 것!
---[비고]---
메모리: 56760 | 시간: 452
for _, start, end in lectures:
    heapq.heappush(ends, end)
    min_end = heapq.heappop(ends)
    if start < min_end:
        cnt += 1
        heapq.heappush(ends, min_end)
뺏다 넣었다 하는 코드의 시간 복잡도가 더 적음 -> 376ms
아마 더 자주 정렬해주어서 매 반복마다 정렬할게 적어져서 그런거같기도하고
같이 논의해보고 싶음

"""
import heapq
import sys


def solution(lectures):
    lectures.sort(key=lambda x: x[1])  # 시작시간 순으로 정렬
    ends = []  # 강의 끝나는 시간 모음 -> heap 사용예정
    cnt = 0  # 배치되는 강의 개수
    for _, start, end in lectures:  # 정렬된 강의 순으로 판단
        heapq.heappush(ends, end)  # 가장 먼저 끝나는 강의 시간을 알기 위해 heap 정렬 사용
        if start < ends[0]:  # 현재 추가된 강의가 가장 빨리끝나는 강의가 끝나기 전에 시작하면
            cnt += 1  # 새로운 강의실 배치 (+1)
        else:  # 현재 추가된 강의가 가장 빨리끝나는 강의가 끝난 후에 시작하면
            heapq.heappop(ends)  # 해당 강의 배치 (+0)

    return cnt


if __name__ == '__main__':
    N = int(input())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(inputs))
