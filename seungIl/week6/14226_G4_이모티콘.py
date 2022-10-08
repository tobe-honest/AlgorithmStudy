# BaekJoon P14226 "이모티콘" (그래프,BFS | G4)
"""
---[실수]---
1트 -> memo 사용 없이 전수 조사 ==> 메모리 초과
2트 -> memo를 1차원적으로만 생각 (curr_cnt로만 visited 판단) ==> 틀림
+) next_cnt 의 범위 설정을 안했었음 -> 2 <= next_cnt <= 1000

∴ memo를 2차원으로 (curr_cnt, clip_cnt 모두 visited 판단) 확인, next_cnt는 가질 수 있는 개수로만 설정
---[부족한 점]---
---[풀이]---
---[비고]---
메모리 : 32544KB | 시간 : 104ms
"""
from collections import deque


def bfs(target_cnt):
    memo = [[0 for _ in range(1001)] for _ in range(1001)] # curr_cnt, clip_cnt visited 기록
    memo[1][0] = 1  # start point
    q = deque([[1, 0, 0]])  # 화면 개수, 클립보드 개수, 시간
    while q:
        curr_cnt, clip_cnt, sec = q.popleft()
        # 붙여넣기 or 한개 제거
        for action in [clip_cnt, -1]:
            next_cnt = curr_cnt + action
            if next_cnt == target_cnt:
                return sec + 1

            if 2 <= next_cnt <= 1000 and not memo[next_cnt][clip_cnt]:
                memo[next_cnt][clip_cnt] = 1
                q.append([next_cnt, clip_cnt, sec + 1])
        # 복사
        if not memo[curr_cnt][curr_cnt]:
            memo[curr_cnt][curr_cnt] = 1
            q.append([curr_cnt, curr_cnt, sec + 1])


def bfs2(target_cnt):
    memo = {(1, 0): 1} # 2차원 리스트가 아닌, 튜플을 key로 갖는 dictionary 생성
    q = deque([[1, 0, 0]])  # 화면 개수, 클립보드 개수, 시간
    while q:
        curr_cnt, clip_cnt, sec = q.popleft()
        # 붙여넣기 or 한개 제거
        for action in [clip_cnt, -1]:
            next_cnt = curr_cnt + action
            if next_cnt == target_cnt:
                return sec + 1

            if 2 <= next_cnt <= 1000 and (next_cnt, clip_cnt) not in memo:
                memo[(next_cnt, clip_cnt)] = 1
                q.append([next_cnt, clip_cnt, sec + 1])
        # 복사
        if (curr_cnt, curr_cnt) not in memo:
            memo[(curr_cnt, curr_cnt)] = 1
            q.append([curr_cnt, curr_cnt, sec + 1])


def solution(s):
    return bfs2(s)


if __name__ == '__main__':
    S = int(input())
    print(solution(S))
