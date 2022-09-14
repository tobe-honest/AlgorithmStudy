# BaekJoon P7576 "토마토" (그래프,BFS | G5)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
일단 1(익은 토마토)의 위치를 모두 알아낸 후
해당 위치들을 bfs 에서 Queue 의 초기값으로 설정 (초기값 : 그래프 탐색 시작 위치 및 depth(day))
즉, 시작 위치는 기존과 다르게 동시에 여러 개가 될 수도 있는 것
그 후 bfs 를 통해 땅따먹기 진행 (0이면 땅따먹기를 하는 걸로, visited 는 따로 두지 않음 -> 1이면 사실상 방문한 것이므로)
땅따먹기의 결과로 마지막으로 익어진 토마토의 day 를 반환.
마지막으로 모든 토마토가 1인지 판단 -> 0 이면 땅따먹기 실패 -> return -1
모든 토마토가 1 -> bfs 의 결과를 반환
---[비고]---
메모리 : 169648 | 시간 : 1940
"""
from collections import deque


def bfs(m, n, start_idxes, box_map):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    day = 0
    q = deque([[i, j, day] for i, j in start_idxes])  # 토마토가 1이었던 모든 위치를 가지고 Queue시작
    while q:
        ci, cj, day = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < n and 0 <= nj < m) and box_map[ni][nj] == 0:
                box_map[ni][nj] = 1 # visited 표시 (-> 익었다는 표현)
                q.append([ni, nj, day + 1])

    return day


def solution(m, n, box_map):
    # bfs 시작 위치 선언 (단일 or 여러개) -> bfs 의 초기값들
    start_idxes = []
    for i in range(n):
        for j in range(m):
            if box_map[i][j] == 1:
                start_idxes.append([i, j])

    # bfs 진행 (땅따먹기)
    result = bfs(m, n, start_idxes, box_map)

    # 모든 토마토들이 익었는지 판단 (not -> , yes -> result)
    for i in range(n):
        for j in range(m):
            if box_map[i][j] == 0:
                return -1

    return result


if __name__ == '__main__':
    M, N = map(int, input().split())
    gmap = [list(map(int, input().split())) for _ in range(N)]
    print(solution(M, N, gmap))
