# BaekJoon P12851 "숨바꼭질2" (그래프,BFS | G4)
"""
---[실수]---
bfs 특성 상
나중에 오는 값이 이전 값보다 작을 수가 없음!!
같은 건 같은 sec(depth)에서 똑같은 애를 접근할 때 발생하는 것
추가로 오는데까지 걸리는 시간에서
memo[move][1] = same_cnt + curr_same_cnt 로 해야 되는걸
memo[move][1] = same_cnt + 1 로 그냥 하나만 더해 틀림
1을 더하는 것이 아닌 해당 동일 경로값을 그대로 가져와서 합쳐줘야 함
---[부족한 점]---
bfs의 특징을 제대로 이해하지 못했었음
-> 먼저 접근 되는 애들이 그 시점의 가장 빠른 경로
-> 즉, 각각의 값들을 비교할 필요없이 visited로 끝낼 수 있는 것
---[풀이]---
일단, n 보다 k가 작은경우, 무조건 -1로 이동밖에 안되므로 return [n-k, 1]
n 보다 k가 큰 경우, bfs 시작
bfs
memo 설정
-> 수빈이나 동생이 위치할 수 있는 모든 범위에서의
현재 위치(idx)에서의 [오는데까지 걸린 시간, 최소 시간으로 현재 위치까지 올 수 있는 경로의 개수]
Q가 빌때까지 돌리면서
다음으로 갈 수 있는 곳에 대해서
만약 다음 갈 곳의 memo가 처음 방문하는 곳이다 -> 걸린 시간, 현재 위치까지 올 수 있는 경로의 개수를 그대로 받아 저장
그리고 q에 저장
만약 다음 갈 곳의 memo가 처음 방문하지 않았고, 걸린 시간이 동일하다
-> 다음 갈 곳의 동일 경로 + 현재 경로 -> 경로를 합쳐줘서 하나로 만들어주는 역할
q에 저장하지 않음 -> 경로를 하나로 합쳤기 때문
---[비고]---
푼 시간: 2시간 30분
메모리 : 42988 | 시간 : 224
"""
from collections import deque


def bfs(n, target):
    memo = [[0, 0] for _ in range(100001)]  # 수빈이나, 동생이 위치할 수 있는 범위
    # memo -> 현재 위치(idx)에서의 [오는데까지 걸린 시간, 최소 시간으로 현재 위치까지 올 수 있는 경로의 개수]
    memo[n] = [0, 1]  # 수빈이의 처음 위치
    q = deque([[n, 0]]) # 수빈이의 위치로 시작
    while q:
        curr, sec = q.popleft() # 현재 위치, 걸린 시간
        curr_same_cnt = memo[curr][1] # 현재 위치까지 올 수 있는 경로의 개수
        for move in [curr - 1, curr + 1, curr * 2]:
            if 0 <= move < len(memo): # 갈 수 있는 위치
                min_sec, same_cnt = memo[move] # 다음 위치의 memo값
                if not min_sec:  # not visited
                    memo[move] = [sec + 1, curr_same_cnt] # 걸린 시간, 현재 위치까지 올 수 있는 경로의 개수를 그대로 받음
                    q.append([move, sec + 1]) # 다음 위치, 걸린 시간 Q에 추가
                elif sec + 1 == min_sec:  # 오는데까지 걸린 시간이 동일
                    memo[move][1] = same_cnt + curr_same_cnt  # 이미 기존의 경로들의 개수에 현재 위치까지 올 수 있는 경로의 개수를 더해줌
                    # 경로들을 하나로 합쳐주는 역할
    return memo[target]


def solution(n, k):
    if n >= k:
        return [n - k, 1]
    return bfs(n, k)


if __name__ == '__main__':
    N, K = map(int, input().split())
    for i in solution(N, K):
        print(i)
