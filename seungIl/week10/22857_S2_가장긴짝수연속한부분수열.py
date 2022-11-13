# BaekJoon P22857 "가장 긴 짝수 연속한 부분 수열" (DP,투 포인터 | S2)
"""
---[실수]---
---[부족한 점]---
인덱스적인 접근에서 실수를 많이함
---[풀이]---
윈도우의 크기가 정해지지 않은 상태에서
늘릴 수 있을 때 까지 늘리고,
늘릴 수 없으면 늘릴 수 있도록 줄인 후 늘리는 방향으로 진행
---[비고]---
풀이시간: 1h
메모리: 35368 | 시간: 116
"""
import sys


def solution(n, k, nums):
    s = 0 # start
    e = 0 # end
    answer = 0 # max of even
    del_cnt = 0 # delete count
    even_cnt = 0 # temp of even count
    while s <= e < n:
        # 삭제 횟수가 k를 넘어섰을 때 -> 시작점 줄여주기 -> 요소들을 더 추가하기 위한 작업
        if del_cnt > k:
            # 시작점이 짝수
            if nums[s] % 2 == 0:
                even_cnt -= 1 # 현재 짝수 개수 -1
                s += 1 # 시작점 오른쪽으로 이동 -> 요소 줄이기
            # 시작점이 홀수
            else:
                del_cnt -= 1 # 삭제 횟수 -1
                s += 1
        else: # 삭제 횟수가 k 이하일 때 -> 끝점 늘려주기
            if nums[e] % 2 == 0:
                even_cnt += 1 # 현재 짝수 개수 +1
                e += 1 # 끝점 오른쪽으로 이동 -> 요소 늘리기
            else:
                del_cnt += 1 # 삭제 횟수 +1
                e += 1

        # if del_cnt < k: # 해도 되고 안해도 됨 (차피 삭제 횟수가 k를 넘어서는 경우는 끝점에서 홀수가 들어오는 경우)
        answer = max(answer, even_cnt)
    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(N, K, inputs))
