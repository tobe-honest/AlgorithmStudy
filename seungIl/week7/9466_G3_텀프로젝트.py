# BaekJoon P9466 "텀프로젝트" (그래프 이론 | G3)
"""
---[실수]---
---[부족한 점]---
1,2,3트 : 시간초과 -> 노드를 하나별로 그룹인지 아닌지 판단 => 중복해서 search를 하는 격
---[풀이]---
시작되는 노드를 통해서 현재 노드가 닿을 수 있는 모든 노드들에 대해서 그룹(싸이클)인지 아닌지 판단
싸이클이 되는 애들에 대해선 모두 그룹으로 처리 -> 0으로 변경
나머지 애들은 건드리지 않음 -> 1 유지

visited와 memo이용
memo
    - 싸이클의 시작점을 찾는데 이용
    - 싸이클을 찾기 시작한 한 단위에서의 visited라고 생각하면 됨
    - 한 단위에서 중복 된다 => 싸이클
    - 중복 되는 그 시점이 싸이클의 시작점이라고 보고 해당 싸이클의 모든 노드를 그룹 처리
visited
    1. 방문처리를 통해 시간을 줄임 -> 한번에 닿을 수 있는 모든 노드를 방문하기 때문에 굳이 또 판단할 필요가 없음
    2. 싸이클인지 아닌지에 대한 판단에 사용 -> memo에서 걸러지지 않은 중복 노드들은 이미 싸이클을 이루었거나 그룹이 되지 못하는 노드에 연결 되는 노드인 것
                                    => 싸이클이 될 수 없음
---[비고]---
풀이 시간 : 1h 8m
메모리 : 52192 | 시간 : 3648
"""
import sys


# 해당 노드를 시작점으로 하는 싸이클의 모든 노드에 대해 그룹 처리
def make_group(curr, friends, result):
    next_friend = friends[curr] - 1
    while next_friend != curr:
        result[next_friend] = 0
        next_friend = friends[next_friend] - 1


def find_cycle(i, friends, visited, result):
    memo = {i} # memo에 중복되는 노드 -> 싸이클의 시작점
    curr = i
    while True:
        visited[curr] = 1 # 방문 기록
        next_friend = friends[curr] - 1 # 다음 갈 노드
        if next_friend in memo: # 다음 갈 노드가 현재 상태에서 방문했던 노드다 -> 싸이클
            result[next_friend] = 0 # 해당 노드는 싸이클을 이루므로 result에 기록
            make_group(next_friend, friends, result) # 해당 노드를 시작점으로 하는 싸이클의 모든 노드에 대해 그룹 처리
            return
        # 다음 노드가 memo에는 없는데 이미 방문한 노드다 -> 이전 상태에서 방문했던 노드
        # => 이미 싸이클을 이루었거나 그룹이 되지 못하는 노드에 연결 되는 노드인 것
        # ==> 싸이클이 될 수 없음
        elif visited[next_friend]:
            return

        # 싸이클인지 아닌지 아직 모르는 노드 -> 더 뻗어 나가야 알 수 있는 노드
        memo.add(next_friend) # 현재 상태에서 방문했다는 것을 기록
        curr = next_friend # 현재 노드 변경


def solution(n, friends):
    result = [1 for _ in range(n)] # 각 노드들이 그룹에 포함되는지 아닌지 기록 (0 -> 그룹, 1 -> not 그룹)
    visited = [0 for _ in range(n)] # 각 노드를 방문했는지 판단
    for i in range(n):
        # 방문하지 않은 노드들에 대해서만 판단
        if not visited[i]:
            # 현재 노드를 어어가다 싸이클이 생성되는 구간이 있는지 판단
            find_cycle(i, friends, visited, result)

    return sum(result)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        inputs = [*map(int, sys.stdin.readline().split())]
        print(solution(N, inputs))
