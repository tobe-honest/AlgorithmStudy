# BaekJoon P5904 "Moo게임" (분할정복, 재귀 | G5)
"""
---[실수]---
1트 -> 54%에서 틀림 보완 필요
=> if k == 0 부분 (맨 밑단) 에서 n이 0부터 시작한다고 착각 -> `moo[n]`
=> but, n 은 1부터 시작 -> `moo[n-1]`
---[부족한 점]---
---[풀이]---
바텀 업 으로 시작 K를 찾고
찾은 K를 통해 탑 다운으로 재귀를 통해 n의 위치에 있는 요소 찾기
1) 시작 k 찾기
일단 k를 늘려가면서 S(k)의 길이를 측정하고
S(k)의 길이가 n 보다 크거나 같은 순간 해당 지점을 시작지점이라고 가정
2) S(k)에서 n의 위치 찾기
S(k) = S(k-1) + 'moo...'[len: k+3] + S(k-1)
로 진행되기 때문에 n의 위치가 왼쪽인지 가운데인지 오른쪽인지 판단
왼쪽,오른쪽이면 S(k-1)로 파고들어가고 가운데 이면 k+3 rule 에 의해서 반환
이때 중요한 것은 오른쪽이면 n의 위치는 오른쪽에 맞게 수정해주어야 함 -> `n - (left + mid)`
---[비고]---
메모리 : 30840 | 시간 : 68
"""


# 시작 K 찾기
def find_k(n):
    prev_len = 3
    k = 1
    while True:
        total_len = prev_len + (k + 3) + prev_len
        if n <= total_len:
            start = k
            break
        prev_len = total_len
        k += 1
    return start, total_len


# S(k)
def s(k, length, n):
    # s(0) 이라면 -> 가장 끝단
    if k == 0:
        moo = list('moo')
        return moo[n - 1]

    # 가운데, 문자열의 길이
    mid = k + 3
    # 왼쪽, 오른쪽, 문자열의 길이
    left = right = (length - mid) // 2

    # 만약 n 이 해당 S(K)의 mid 에 위치한다면
    if left < n <= left + mid:
        idx = n - left
        if idx == 1:
            return 'm'
        else:
            return 'o'

    # n 이 해당 S(K)의 왼쪽에 위치한다 -> S(K-1)로 search
    elif n <= left:  # left
        return s(k - 1, left, n)
    # n 이 해당 S(K)의 오른쪽에 위치한다 -> S(K-1)로 serach
    else:  # right => 여기서 중요한 건 n을 오른쪽의 입장에서 값을 변경하여 보내주어야함
        return s(k - 1, right, n - (left + mid))  # 오른쪽 입장에서의 n 위치 -> n - (left+mid)


def solution(n):
    start, total_len = find_k(n)  # 시작 K 찾기
    return s(start, total_len, n)  # 해당 K로 S(K)에서 n번째 요소 찾기


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
