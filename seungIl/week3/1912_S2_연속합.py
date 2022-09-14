# BaekJoon P1912 "연속합" (DP | S2)
"""
---[실수]---
---[부족한 점]---
점화식을 생각해내는 능력 부족
한단계만을 거쳐서 풀려고 함 -> dp[-1]
두단계를 거쳐서 답을 낼 수도 있다는 생각 필요 -> max(dp)
---[풀이]---
dp -> 혼자있을 때 vs 뭉쳐있을 때
max(dp) -> 혼자있든 뭉쳐있든 그 무리 중에서 가장 큰 값

dp[i] = max(li[i], dp[i-1]+li[i])
현재 저장할 값 = max(자기 혼자 있을 때, 혼자가 아닌 뭉쳐있을 때)
 -> 무리를 이어갈지 안이어갈지에 대한 판단
 max(dp) -> 그런 무리들 중에서 최대 값
---[비고]---
"""
import sys


def solution(n, li):
    dp = [i for i in li]
    for i in range(1,n):
        dp[i] = max(li[i], dp[i-1]+li[i])

    return max(dp)

if __name__ == '__main__':
    N = int(input())
    li = list(map(int, sys.stdin.readline().split()))
    print(solution(N, li))
