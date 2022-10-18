# BaekJoon P14503 "로봇청소기" (구현, 시뮬레이션 | G5)
"""
---[실수]---
---[부족한 점]---
사실 현재 방향에서 갈 수 있는 방향의 선택지가 여러가지가 아닌 "하나"이기 때문에
bfs를 쓸 필요 없이 그냥 기본 graph에서 index로 접근해도 됐었음
---[풀이]---
bfs를 통해 품
계속 왼쪽으로 회전하면서 청소할 수 있는 애가 발견되면 그 애로 넘어가고
모든 방향에 대해서 청소할 수 있는 공간이 없다 -> 후진
    - 후진 시 뒤가 벽이다 => 종료
    - 후진 시 뒤가 청소를 했던 공간이다 => 뒤로 이동 (후진 진행)
---[비고]---
풀이 시간 : 24m
메모리 : 32508 | 시간 : 88
"""
import sys
from collections import deque


def bfs(n, m, r, c, d, graph):
    di = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    q = deque([[r, c, d]])
    result = 1
    while q:
        ci, cj, cd = q.popleft()
        # 2, 1
        for i in range(1, 6):
            # 2-3, 2-4
            if i == 5:
                nd = (cd + 2) % 4  # 반대 방향
                ni, nj = ci + di[nd][0], cj + di[nd][1]  # 반대 방향 위치
                # 2-4
                if (0 <= ni < n and 0 <= nj < m) and graph[ni][nj] == 1: # 뒤가 벽
                    return result # 종료
                else:  # 2-3
                    q.append([ni, nj, cd]) # 뒤로 이동 (현재 방향은 유지한채로)

            # 2-1, 2-2
            nd = (cd - i) % 4  # 왼쪽 방향
            ni, nj = ci + di[nd][0], cj + di[nd][1]  # 왼쪽 방향 위치
            if (0 <= ni < n and 0 <= nj < m) and graph[ni][nj] == 0:  # 청소 가능
                graph[ni][nj] = -1  # 1. 현재 위치 청소
                result += 1  # 청소 결과 개수 + 1
                q.append([ni, nj, nd])  # 이동
                break

    return result


def solution(n, m, r, c, d, graph):
    graph[r][c] = -1
    return bfs(n, m, r, c, d, graph)


if __name__ == '__main__':
    N, M = map(int, input().split())
    R, C, D = map(int, input().split())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, M, R, C, D, inputs))
