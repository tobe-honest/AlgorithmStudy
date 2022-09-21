# BaekJoon P2206 "벽 부수고 이동하기" (그래프 | G3)
"""
---[실수]---
1,2트 -> memo를 하나만 두고 진행함
3~7트 -> 등호를 잘못둠 -> 같은거 까지 고려하게 해버림 (고려할 필요가 없는데)
    -> 이거땜에 시간초과, 메모리초과 오지게 뜨고 2시간 날림 부등호 하나로
가장 큰 실수
- 현재까지 온 거리가 동일하다면 굳이 그 값에 대해 고려할 필요 없음 -> 차피 동일한 상태에서 또 뻗어가는 것이므로
    => if (cnt + 1) < memo[ni][nj]
- 2시간동안 헤멤
---[부족한 점]---
푸는 시간이 길어질 수록 대강 빨리 풀려고만 하는 경향이 있음
---[풀이]---
벽을 뚫은 상태와 벽을 뚫지 않은 상태를 구분해주어야 함 -> (memo_0, memo_1)
=> 이유 : 벽을 뚫고 보니 나중에 또 벽이 있어서 도착지점에 도달하지 못하는 경우가 있음
         즉, 먼저 벽을 뚫지 않고 나중에 벽을 뚫어야되는 경우가 있는 것
=> 즉, 마지막까지 벽을 뚫지 않은 상태의 경로를 살려두는 것

Q
다음 갈 곳이 벽이 아닌 경우,
    현재 내가 벽을 이미 뚫었는지 안 뚫었는지 판단하고 (값을 따로 비교하기 위함)
        뚫은 상태라면, 벽을 뚫은 기존 경로보다 현재 경로가 더 짧은 지 판단 (짧다면 기록값을 변경하고 q에 추가)
        뚫지 않은 상태라면, 벽을 뚫지 않은 기존 경로보다 현재 경로가 더 짧은지 판단 (짧다면 기록값을 변경하고 q에 추가)
다음 갈 곳이 벽인 경우,
    현재 내가 벽을 이미 뚫었는지 안 뚫었는지 판단하고 (해당 벽을 뚫을 수 있는지 확인)
        뚫은 상태라면, 고려할 필요가 없음
        뚫지 않은 상태라면, 벽을 뚫고, 벽을 뚫지 않은 기존 경로보다 현재 경로가 더 짧은지 판단 (짧다면 기록값을 변경하고 q에 추가)

마지막으로 벽을 뚫지 않고 도달한 최소값과 벽을 뚫고 도달한 최소값을 비교하여 결과 값 반환
---[비고]---
메모리 : 145036 | 시간 : 4100
"""

import sys
from collections import deque


def bfs(n, m, gmap):
    memo_0 = [[float('inf') for _ in range(m)] for _ in range(n)]  # (0) 벽을 뚫지 않은 상황에서의 최솟값 기록
    memo_1 = [[float('inf') for _ in range(m)] for _ in range(n)]  # (1) 벽을 뚫은 상황에서의 최솟값 기록
    memo_0[0][0] = 1  # 출발점 -> cnt = 1
    memo_1[0][0] = 1  # 출발점 -> cnt = 1

    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque([[0, 0, 1, True]])  # 현재 위치(r,c), 개수, 벽을 뚫을 수 있냐
    while q:
        ci, cj, cnt, can_break = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                # 벽이 아닌 경우
                if gmap[ni][nj] == 0:
                    if can_break: # 벽을 뚫지 않은 상태 => memo_0과 비교
                        if (cnt + 1) < memo_0[ni][nj]: # 벽을 뚫지 않은 기존 경로보다 현재 경로가 더 짧다
                            memo_0[ni][nj] = cnt + 1
                            q.append([ni, nj, cnt + 1, can_break])
                    else: # 이미 한번 벽을 뚫은 상태 => memo_1과 비교
                        if (cnt + 1) < memo_1[ni][nj]: # 벽을 뚫은 기존 경로보다 현재 경로가 더 짧다
                            memo_1[ni][nj] = cnt + 1
                            q.append([ni, nj, cnt + 1, can_break])
                # 벽인 경우
                else:
                    # 벽을 뚫지 않은 상태 -> 벽을 뚫 수 있음 => memo_1과 비교
                    if can_break:
                        if (cnt + 1) < memo_1[ni][nj]: # 벽을 뚫은 기존 경로보다 현재 경로가 더 짧다
                            memo_1[ni][nj] = cnt + 1
                            q.append([ni, nj, cnt + 1, False])

    if memo_0[-1][-1] == float('inf') and memo_1[-1][-1] == float('inf'):
        return -1
    return min(memo_0[-1][-1], memo_1[-1][-1])


def solution(n, m, gmap):
    return bfs(n, m, gmap)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    print(solution(N, M, graph))
