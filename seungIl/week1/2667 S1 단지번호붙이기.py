# BaekJoon P2667 "단지번호붙이기" ( 그래프, BFS, DFS| S1)
"""
<유형: 그래프, BFS, DFS >
---[실수]---
bfs 에서의 cnt 를 언제해야되는지 햇갈려서 한번 실수
cnt 는 맨 처음에 0으로 설정하고
매번 Queue 에서 값을 꺼내올 때 마다 +1 하는 것으로 설정
값을 꺼낼 때 -> 해당 지점에 도달했다고 판단 (이때 +1 해주는 것이 적절함)
---[부족한 점]---
---[풀이]---
땅따먹기라고 생각
가장 먼저 bfs 를 시작할 수 있는 지점에 대해서 bfs 를 시작
그리고 가능한 지점에 대해서 땅따먹기 시작
땅따먹기가 완료된 지점에 대해선 -1을 통해 이미 방문 한 곳이라고 설정 (따로 visited 를 생성하지 않음)
즉, 땅따먹기가 가능한 지점은 1만이 가능 (문제의 조건과 visited 를 한번에 해결 가능)
bfs 의 결과를 해당 땅따먹기의 cnt 로 반환 하여 나중에 종합적으로 sort 진행
bfs 를 시작할 때 마다 총합에 +1 을 통해 단지 수 측정
---[비고]---
이미 풀어본 문제여서 금방 푼 듯
+ 해당 풀이에서 추가적으로 최적화할 수 있는 부분이 있는지 궁금함
"""

from collections import deque
import sys

di = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(i, j, gmap):
    n = len(gmap)
    cnt = 0
    q = deque([[i, j]])
    while q:
        ci, cj = q.popleft()
        cnt += 1
        for ti, tj in di:
            ni, nj = ci + ti, cj + tj
            if (0 <= ni < n and 0 <= nj < n) and gmap[ni][nj] == 1:
                gmap[ni][nj] = -1
                q.append([ni, nj])

    return cnt


def solution(n, gmap):
    cnt = 0
    result = []
    for i in range(n):
        for j in range(n):
            if gmap[i][j] == 1:
                cnt += 1
                gmap[i][j] = -1
                result.append(bfs(i, j, gmap))
    result.sort()
    print(cnt)
    for i in result:
        print(i)


if __name__ == '__main__':
    N = int(input())
    gmap = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    solution(N, gmap)
