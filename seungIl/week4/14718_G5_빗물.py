# BaekJoon P14718 "빗물" (구현, 시뮬레이션 | G5)
"""
---[실수]---
시작할때부터 비어있는 벽에 대해 고려하지 않아서
cnt 가 벽이 없는 구간까지 고려하게 됨
즉, cnt는 벽이 세워져 있는 상태에서만 count 되어야 함
    -> if start !=0 : cnt += 1
---[부족한 점]---
구현에서 항상 놓치는 부분이 너무나 많음
-> 주어진 예제 말고도 직접 예제를 생각해서 테스트 해봐야 될듯
-> 발생할 수 있는 모든 경우를 생각해낸 후 그에대한 코드를 작성해야됨
---[풀이]---
먼저 2차원 배열을 생성하여
벽에 맞게 그래프를 만들어주고
아래부터 테트리스 마냥 확인하는 것
벽-> start
벽이 발견될 때마다 start를 1씩 추가해주고
start가 1일 때 (벽이 세워짐) 빈공간에 대한 cnt를 늘려주고
start가 2일 때 (벽이 닫힘 -> 물 저장됨) 지금까지 기록된 cnt를 반영
---[비고]---
메모리 : 31100 | 시간 : 100
"""
import sys

def solution(h, w, walls):
    wall_graph = [[0 for _ in range(w)] for _ in range(h)]

    for j, repeat in enumerate(walls):
        for i in range(repeat):
            wall_graph[(h-1)-i][j] = 1

    answer = 0
    for i in range(h-1, -1, -1):
        start = 0
        cnt = 0
        for j in range(w):
            if wall_graph[i][j] == 1:
                start += 1
            else:
                if start != 0:
                    cnt += 1
            if start == 2:
                answer += cnt
                start = 1
                cnt = 0
    return answer


if __name__ == '__main__':
    H, W = map(int, input().split())
    inputs = [*map(int, sys.stdin.readline().split())]
    print(solution(H, W, inputs))
