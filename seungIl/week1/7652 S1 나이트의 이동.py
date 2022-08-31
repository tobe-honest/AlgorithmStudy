# BaekJoon P7652 "나이트의 이동" ( BFS | S1)
"""
<유형: 그래프, BFS>
---[실수]---
없음
---[부족한 점]---
시간이 1936ms -> 최적화 여지 충분
---[풀이]---
냅다 BFS 를 떄린 것
이론상 BFS 시 가장 먼저 원하는 지점에 도착하는 경우가 가장 최단 경로 이므로
추가적인 설정과 조건 없이 그냥 가장 먼저 도착할 경우 해당 cnt(이동 횟수)를 반환
또한 visited를 따로 두지 않고 gmap의 원소가 0이면 방문하지 않았다고 가정하고
gmap 이 0이 아닌 곳(visited)에 대해선 search 하지 않도록 설정.
---[비고]---
(최적화가 가능한지 의논하고 싶은 문제)
"""
import sys
from collections import deque


def bfs(gmap, si, sj, ei, ej):
    m = len(gmap)
    di = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
    q = deque([[si, sj, 0]])
    while q:
        ci, cj, cnt = q.popleft()
        if (ci, cj) == (ei, ej):
            return cnt
        for ti, tj in di:
            ni, nj = ci + ti, cj + tj
            if (0<=ni<m and 0<=nj<m) and gmap[ni][nj] == 0:
                gmap[ni][nj] = cnt
                q.append([ni,nj,cnt+1])


def solution(m, si, sj, ei, ej):
    gmap = [[0 for _ in range(m)] for _ in range(m)]
    return bfs(gmap, si, sj, ei, ej)


if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        m = int(sys.stdin.readline().strip())
        si, sj = map(int, sys.stdin.readline().split())
        ei, ej = map(int, sys.stdin.readline().split())
        print(solution(m, si, sj, ei, ej))
