# BaekJoon P10026 "적록색약" ( | S1)
"""
---[실수]---
ci, cj 와 함수로 받아온 인자인 i,j 를 헷갈려서 cmap[i][j] 를 계속 넣음
bfs 시작 위치에서 visited의 표시인 ‘V’ 를 bfs 전에 표시해주면 bfs 안에서 동일한 값에 대해 땅따먹기를 시작하기 때문에 ‘V’값만을 찾게됨 → 오류
---[부족한 점]---
실수가 너무 잦음. 마음이 급해서 빨리 풀려고 해서 생각이 짧아지고 실수가 많아짐
---[풀이]---
이전 단지구하기와 굉장히 유사한 문제
일단 색약과 보통사람을 구분하고 (지도를 2개로 생성 → blind_map, normal_map)
색약의 지도에서 ‘G’ 를 ‘R’ 로 변경하여 ‘G’와’R’ 을 동일하게 보도록 설정
그 후 색약, 보통사람 각각 bfs 시작
 각각의 위치에 대해서 bfs 가 가능하다 → 개수추가 및 bfs 안으로 들어가서 해당 위치의 값과 동일한 애들에 대해서 땅따먹기
중요한 점 : visited 를 따로 두지 않고 gmap 에 ‘V’ 표시 → 시작 위치는 bfs() 종료 후 체크해줌
---[비고]---
메모리 : 32508 | 시간 : 112
"""
import sys
from collections import deque


def bfs(i, j, n, cmap):
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    q = deque([[i, j, cmap[i][j]]])
    while q:
        ci, cj, val = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            if (0 <= ni < n and 0 <= nj < n) and cmap[ni][nj] == val:
                cmap[ni][nj] = 'V'
                q.append([ni, nj, val])


def solution(n, gmap):
    blind_map = []
    for i in range(n):
        temp = []
        for j in range(n):
            val = gmap[i][j]
            if val == 'G':
                temp.append('R')
            else:
                temp.append(val)
        blind_map.append(temp)

    # normal
    normal_result = 0
    for i in range(n):
        for j in range(n):
            if gmap[i][j] != 'V':
                normal_result += 1
                bfs(i, j, n, gmap)
                gmap[i][j] = 'V'

    # blind
    blind_result = 0
    for i in range(n):
        for j in range(n):
            if blind_map[i][j] != 'V':
                blind_result += 1
                bfs(i, j, n, blind_map)
                blind_map[i][j] = 'V'

    return normal_result, blind_result


if __name__ == '__main__':
    N = int(input())
    gmap = [list(list(sys.stdin.readline().strip())) for _ in range(N)]
    print(*solution(N, gmap))
