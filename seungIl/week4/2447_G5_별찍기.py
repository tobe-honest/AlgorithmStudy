# BaekJoon P2447 "별찍기-10" (분할정복, 재귀 | G5)
"""
---[실수]---
---[부족한 점]---
분할정복 구현에 항상 대가리가 잘 안 돌아감
---[풀이]---
분할하여 정복하면서 *을 찍어주는 방향이 아닌
미리 *을 다 찍어주고 빈 공간이어야만 하는 부분에 대해서 '*'을 ' '로 바꿔서 빈 공간 처리 진행
즉, 빈공간만 따로 처리해주는 것
---[비고]---
메모리 : 68760 | 시간 : 800
"""


# 빈 공간 처리
def make_clean(si, sj, volume, answer):
    for i in range(si, si + volume):  # 시작 인덱스 ~ 시작엔덱스 + volume(step = ... -> 9 -> 3 -> 1)
        for j in range(sj, sj + volume):
            answer[i][j] = ' '


# 분할 정복, 3*3 트리
def conquer(start, step, answer):
    ci, cj = start

    if step == 1:
        make_clean(ci+step,cj+step,step,answer)
        return

    # 3x3 분할
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 오로지 빈 공간인 부분의 시작 지점
                make_clean(ci + step, cj + step, step, answer) # 모두 빈칸 처리
            else: # 분할
                conquer([ci + i * step, cj + j * step], step // 3, answer)


def solution(n):
    # 일단 모든 별을 채우고 시작
    answer = [['*' for _ in range(n)] for _ in range(n)]
    conquer([0, 0], n // 3, answer) # 분할 시작
    for i in range(n):
        print(''.join(answer[i]))


if __name__ == '__main__':
    N = int(input())
    solution(N)
