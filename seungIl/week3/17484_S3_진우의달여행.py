# BaekJoon P17484 "진우의 달 여행" (DP | S3)
"""
---[실수]---
1단계로만 생각해버림 -> 2단계를 생각할 필요가 있음
---[부족한 점]---
DP에 익숙하지 않음. 계속해서 풀어봐야 될듯
---[풀이]---
DP의 한 공간(dp[i][j])에 저장되는 값은
[왼쪽을 선택했을 대의 최소값, 가운데를 선택했을 때의 최솟값, 오른쪽을 선택했을 때의 최솟값]
최적 값 판단 로직 (dp[i][j]의 값을 확정 짓는 것)
일단 내가 선택할 수 있는 것 측정 (리스트의 맨왼쪽이면 왼쪽을 택할 수 없음 등)
1. 왼쪽을 선택했을 때의 값 저장 (dp[i][j][0])
    - 왼쪽의 위치에 따른 값 = dp[i-1][j-1] -> [왼 , 가 , 오]
    - 저장될 값 = 왼쪽을 제외한 "가운데,오른쪽 값의 최솟값" + 왼쪽의 값
    => dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + graph[i - 1][j - 1]
2. 가운데를 선택했을 대의 값 저장 (dp[i][j][1])
3. 오른쪽을 선택했을 때의 값 저장 (dp[i][j][2])
결론적으로 마지막 dp[-1] 에는 각각의 위치에서 왼,가,오 를 선택했을 때의 최솟값이 저장되어 있음
그럼 이제 각각의 왼,가,오,의 최소값 + 자신의 값 중 최솟값을 반환하면 최종 최솟값
=> min(min_result, min(dp[-1][j]) + graph[-1][j])
---[비고]---
메모리 : 30840 | 시간 : 72
"""
import sys


def solution(n, m, graph):
    dp = [[[0, 0, 0] for _ in range(m)]] + [[[sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(m)] for _ in
                                            range(1, n)]
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i - 1][j]
                dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + graph[i - 1][j + 1]
            elif j == m - 1:
                dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + graph[i - 1][j - 1]
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i - 1][j]
            else:
                dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + graph[i - 1][j - 1]
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i - 1][j]
                dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + graph[i - 1][j + 1]

    min_result = sys.maxsize
    for j in range(m):
        min_result = min(min_result, min(dp[-1][j]) + graph[-1][j])

    return min_result


if __name__ == '__main__':
    N, M = map(int, input().split())
    road = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution(N, M, road))
