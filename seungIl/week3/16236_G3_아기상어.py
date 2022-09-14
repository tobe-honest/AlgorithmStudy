# BaekJoon P16236 "아기상어" (그래프 | G3)
"""
---[실수]---
따로 후보를 두고 정렬하지 않고도 애초에 탐색 시 위, 왼쪽, 오른쪽, 아래 순으로 진행하면
조건을 맞출 수 있다고 생각함
+ 먹고 나서 빈칸이라는 표시를 생략함
---[부족한 점]---
너무 단순하게 생각.
또한, 이렇게하면 되겠지~ 식의 마인드가 강했음
생각하지 못한 부분에서 놓치지 않도록 애초에 완벽한 로직을 짜는 것이 중요
---[풀이]---
먼저 현재 상어의 위치에서 BFS 시작
BFS : 먹을 수 있는 물고기를 모두 search 하여 후보군을 생성하고,
      후보들 중 가장 가깝고 가장 위, 가장 왼쪽에 있는 얘를 먹도록 설정
그 후 현재 size 만큼 물고기를 먹게 되면 size를 키우며 먹을 수 있는 물고기의 범위를 늘려줌
이를 반복적으로 돌며 먹을 수 있는 물고기가 없어질 때 까지 진행
---[비고]---
아기상어 -> 상하좌우 , 같거나 작은 물고기
          작은 물고기는 먹을 수 있음
          크기만큼 물고기의 개수를 먹으면 크기+1
"""
import heapq
from collections import deque

# 먹을 수 있는 물고기 중 가장 가까우며 가장 위쪽,왼쪽에 있는 물고기를 먹기위한 BFS
def bfs(graph, curr, size):
    n = len(graph)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    d = [[-1, 0], [0, -1], [0, 1], [1, 0]]  # 위, 왼쪽, 오른쪽, 아래 순으로. (상관없음)
    q = deque([[0, *curr]])
    visited[curr[0]][curr[1]] = 1
    candidates = []
    while q:
        cnt, ci, cj = q.popleft()
        for di, dj in d:
            ni, nj = ci + di, cj + dj
            # 갈 수 있는 공간
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and graph[ni][nj] <= size:
                    visited[ni][nj] = 1
                    # 먹을 수 있는 물고기
                    if 0 < graph[ni][nj] < size:
                        heapq.heappush(candidates, [cnt + 1, ni, nj]) # 후보 등록
                    # 먹을 수는 없지만 지나갈 수 있는 물고기
                    else:
                        q.append([cnt + 1, ni, nj])

    # 먹을 수 있는 물고기 중 가장 가까우며 가장 위, 가장 왼쪽에 있는 물고기 Eating
    if candidates:
        cnt, ci, cj = heapq.heappop(candidates)
        graph[ci][cj] = 0 # 먹음
        return 1, [ci, cj], cnt # +1, 현재 상어 위치, 총 이동 시간(거리)

    return 0, curr, 0


def solution(n, graph):
    curr = [0, 0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:  # BFS 시작 지점 (상어의 위치)
                graph[i][j] = 0
                curr = [i, j]

    eaten = 1 # 먹었느냐 못먹었느냐 (0,1)
    size = 2 # 아기상어의 크기 (이와 같거나 작은 물고기를 지나칠 수 있으며, 이보다 작은 물고기는 먹을 수 있음)
    cnt = 0 # 사이즈가 커지고 나서 먹은 물고기 개수 -> size 를 키우는 기준
    answer = 0 # 총 지난 시간

    # 아무것도 못먹는 상황이면 종료
    while eaten:
        eaten, curr, total = bfs(graph, curr, size) # 먹었느냐 못먹었느냐, 이동 후 상어의 위치, 이동 후 총 지난 시간(거리)
        answer += total
        cnt += eaten # 현재 size에서 먹은 개수 누적
        if cnt == size:  # 먹은 개수가 사이즈와 동일
            size += 1  # 사이즈 UP!
            cnt = 0  # cnt 초기화!

    return answer


if __name__ == '__main__':
    N = int(input())
    gmap = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, gmap))
