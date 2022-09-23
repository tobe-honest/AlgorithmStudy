# BaekJoon P9205 "맥주 마시면서 걸어가기" ( 그래프, BFS | S1)
"""
---[실수]---
처음에 문제를 잘못 이해(편의점을 주어진 순서대로 탐색해야되는 줄 알았음)해서
bfs 가 아닌 일반적인 for 문을 통해서 탐색 -> 실패
```
for ni, nj in orders:
    ni, nj = ni//50, nj//50
    d = abs(ni-ci) + abs(nj-cj)
    if d > 20:
        return 'sad'
    ci, cj = ni, nj
```
---[부족한 점]---
매번 지도 속 그래프로만 생각해서 푸는데 좀 오래 걸림
이 문제는 지도(4방향 이동가능 지도)로 생각하는 것이 아닌. 부모, 자식의 노드 그래프로 생각해서 탐색해야 함
---[풀이]---
현재 좌표에서 종료 지점까지 맥주 20병으로 갈 수 있는 지 check
갈 수 있다 -> `return 'happy'`
갈 수 없다 ->
    현재 좌표에서
    갈 수 있는 모든 곳 (맥주 20병으로 갈 수 있는 거리 and 방문하지 않은 곳 -> `if math.ceil(nd / 50) <= 20 and not visited[idx]`)
    에 접근(`q.append([ni,nj]`) , 방문 표시 -> visited[idx] = 1)
Queue 가 종료될 때 까지 갈 수 있는 상황이 발생하지 않는다 -> return 'sad'
---[비고]---
지금까지 계속 풀었던 그래프 탐색이랑 살짝 다르게 접근해야 돼서 신선했던 문제
메모리 : 34600 KB | 시간 : 108 ms
"""
import math
import sys
from collections import deque


def bfs(n, start, end,  orders):
    si, sj = start
    ei, ej = end
    q = deque([[si,sj]])
    visited = [0 for _ in range(n)]

    while q:
        ci, cj = q.popleft()
        d = abs(ei - ci) + abs(ej - cj) # 현재 좌표와 종료 지점과의 거리 측정
        if math.ceil(d / 50) <= 20: return 'happy' # 갈 수 잇는 거리다 -> 종료

        # 갈 수 없는 거리 -> 현재 좌표에서 갈 수 있는 모든 곳에 대해 접근
        for idx, val in enumerate(orders):
            ni, nj = val
            nd = abs(ni-ci) + abs(nj-cj)
            if math.ceil(nd / 50) <= 20 and not visited[idx]: # 갈 수 있는 곳에 대해 접근
                visited[idx] = 1
                q.append([ni,nj])

    return 'sad'

def solution(n, start, end,  orders):
    return bfs(n, start, end,  orders)



if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        start = list(map(int,sys.stdin.readline().split()))
        orders = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
        end = list(map(int,sys.stdin.readline().split()))
        print(solution(n,start,end,orders))