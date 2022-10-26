# BaekJoon P2559 "수열" (투 포인터, 윈도우 | S3)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
투 포인터 이용.
k개의 수를 담는 윈도우의 시작점과 끝점에 포인터를 두고
윈도우가 한칸 씩 슬라이딩 될 때 마다 끝 포인터의 수를 더해주고, 시작 포인터의 수를 빼줌
위의 결과 중 가장 큰 합을 반환
---[비고]---
풀이 시간 : 15m
메모리: 39572 | 시간 : 112
"""
import sys

# 시간초과 고려 X
def solution_before(k,nums):
    answer = -float('inf')
    for window in zip(*[nums[i:] for i in range(k)]):
        answer = max(answer, sum(window))

def solution(n, k,nums):
    answer = temp = sum(nums[:k])
    for plus in range(k,n):
        minus = plus - k
        temp -= nums[minus]
        temp += nums[plus]
        answer = max(answer, temp)

    return answer

if __name__ == '__main__':
    N, K = map(int, input().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(N,K,inputs))