# BaekJoon P1074 "Z" (분할정복,재귀 | S1)
"""
---[실수]---
1,2트 : 시간초과 -> 모든 재귀를 훑은 점 (2^15*2^15)
3,4트 : 출력초과 -> 값 설정 오류 (cnt = cnt + 2**step 으로 해버림 -> 2의 step 제곱이 아니라 step 의 2 제곱이어야 함) => 값이 겁나 커져버림
---[부족한 점]---
여전히 재귀에서 머리가 제대로 돌아가지 않음.
추가로 집중력 저하로 값 설정에 있어서 실수가 잦았음
+ 부가적인 계산 없이 일단락적으로 계산 식을 넣는 경향이 있음 -> 고칠 필요가 있음
---[풀이]---
분할정복으로 풀지만, 모든 파트를 분할하여 계산하면 안됨 -> 시간초과
target 이 있는 위치만 분할을 통해 세부적인 값을 설정하고
target 이 해당되지 않는 위치는 뛰어넘으면서 해당 계산 값을 넘겨주면 됨
---[비고]---
메모리 30840 시간 68
"""


def conquer(answer, n, curr, cnt, target): # 분할 정복
    ci, cj = curr
    r, c = target

    # target 에 도착
    if n == 1:
        answer[0] = cnt
        cnt += 1
        return cnt

    step = n // 2 # 분할

    for i in range(2):
        for j in range(2):
            # 다음 conquer 할 시작 idx
            ni = ci + step * i
            nj = cj + step * j
            # target 이 해당 다음 위치에 들어가 있는 지 판단
            if ni <= r < ni + step and nj <= c < nj + step: # 들어 가 있으면 해당 위치 계속 conquer 진행
                cnt = conquer(answer, step, [ni, nj], cnt, target) # 분할 후 정복 값(cnt) 반환
            else: # 해당 위치에 포함되어 있지 않다면 conquer 하지 않고
                cnt = cnt + step ** 2  # 다음 분할 위치로 넘어감과 동시에 cnt 를 해당 위치를 건너뛴 만큼 +
    return cnt


def solution(n, r, c):
    answer = [0]
    conquer(answer, 2 ** n, [0, 0], 0, [r, c])  # 분할 정복
    return answer[0]


if __name__ == '__main__':
    n, r, c = map(int, input().split())
    print(solution(n, r, c))
