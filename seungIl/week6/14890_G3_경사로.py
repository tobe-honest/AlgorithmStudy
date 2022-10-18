# BaekJoon P14890 "경사로" (구현 | G3)
"""
---[실수]---
---[부족한 점]---
while문으로 해결하려 함
---[풀이]---
각 라인에 대해서 경사로를 설치할 수 있는지 판단
처음에는 while문으로 그대로 경사로를 한번에 설치하려 했지만,
existed를 통해서 한 칸씩 탐색. -> 경사로가 존재하냐 안하냐를 구분하기 위함
---[비고]---
메모리 : 30840 | 시간 : 72
"""
import sys


def check(road, n, l):
    existed = [0 for _ in range(n)]
    for i in range(1, n):
        if road[i] == road[i - 1]: continue
        if abs(road[i] - road[i - 1]) > 1: # 차이가 1이상
            return 0
        if road[i] > road[i - 1]: # 높은 경우
            for j in range(l):
                # 범위 벗어나거나 같은 길이가 아니거나 이미 경사로가 설치되어 있으면
                if i - j - 1 < 0 or road[i - 1] != road[i - j - 1] or existed[i - j - 1]:
                    return 0
                if road[i - 1] == road[i - j - 1]: # 같은 높이면 경사로 일부 설치
                    existed[i - j - 1] = 1
        elif road[i] < road[i - 1]: # 낮은 경우
            for j in range(l):
                if i + j >= n or road[i] != road[i + j] or existed[i + j]:
                    return 0
                if road[i] == road[i + j]:
                    existed[i + j] = 1

    return 1


def solution(n, l, graph):
    answer = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(graph[i][j])
        answer += check(temp, n, l)
    for j in range(n):
        temp = []
        for i in range(n):
            temp.append(graph[i][j])
        answer += check(temp, n, l)

    return answer


if __name__ == '__main__':
    N, L = map(int, input().split())
    inputs = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
    print(solution(N, L, inputs))
