# BaekJoon P1629 "곱셈" (수학, 분할정복을 통한 재귀 | S1)
"""
---[실수]---
1,2트 -> 모듈러를 가장 나중에 조짐
    즉, search_tree 를 통해서 a의 b 제곱을 계산하고
    마지막에 모듈러 진행 (수정 -> 매 순간마다 모듈러 계산이 필요함)
---[부족한 점]---
분할정복으로 풀어야 겠다는 생각을 잘하지 못함
문제를 보고 수학적으로 Greedy 하게 규칙이나 특이점을 찾아 해결하려 함
분할정복 유형을 많이 풀어봐야 할듯
---[풀이]---
이진분할정복느낌으로 진행
b(제곱수)를 계속해서 반으로 쪼개고 (분할)
반으로 쪼갠 값을 2제곱하여 모듈러 진행 (정복)
ex) 10**16 -> (10**8)^2 -> ((10**4)^2)^2 -> ...
이렇게 되면 16번 반복되어야할 것들이 4번으로 줄어듦
N -> log(N)
---[비고]---
메모리 30840 시간 72
"""


def binary_conquer(a, b, c):
    if b == 1:
        return a % c
    if b % 2 != 0:
        return (binary_conquer(a, b // 2, c) ** 2 * a) % c
    return (binary_conquer(a, b // 2, c) ** 2) % c


def solution(a, b, c):
    return binary_conquer(a, b, c)


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(solution(A, B, C))
