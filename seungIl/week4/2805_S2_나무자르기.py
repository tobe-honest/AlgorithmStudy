# BaekJoon P2805 "나무자르기" (이분탐색 | S2)
"""
---[실수]---
M미터를 딱 가져오는 것이 아니라 "적어도 M미터"
-> M미터 이상의 나무를 가져오기 위해 설정할 수 있는 절단기 높이의 최댓값
1트 -> target과 taken이 같을 때도 더 큰 mid를 가질 수 있는지에 대한 search를 진행하지 않음
---[부족한 점]---
문제 똑바로 읽자
---[풀이]---
참고 : 잘라서 가져온 나무가 작을 수록 절다기의 높이가 커져서 좋은 것
이분탐색의 대상 : 절단기 높이(의 최대값) -> mid(height)
이분탐색의 대상이 적절한 대상인지 판단하는 조건 : 자르고 가져오는 나무의 크기 -> taken

절단기의 높이(mid)를 이분탐색으로 탐색을 하며 -> binary_search()
해당 탐색된 mid값(height, 절단기의 높이)을 통해
현재 mid값이 조건에 맞는 지 판단 -> check()
만약 해당 mid값을 통해 taken(얻은 나무의 양)이 M(target)미터 보다 크거나 같다면
절단기의 높이의 최대값을 찾고 있기 때문에
탐색 범위를 높여(start = mid + 1) 더 높은 절단기의 높이에서도 taken(얻은 나무의 양)이 M(target)미터 보다 크거나 같은지 판단
해당 mid값을 통해 taken(얻은 나무의 양)이 M(target)미터 보다 작다면
탐색 범위를 낮춰(end = mid - 1) 더 낮은 절단기의 높이로 다시 탐색할 수 있도록 설정
! 결론적으로 M보다 크거나 같은데 M이랑 가장 가까운 값을 얻게끔하는 mid(절단기의 높이)를 찾는 것
---[비고]---
메모리 : 148396 | 시간 : 3440
"""
import sys


def check(trees, height):
    taken = 0
    for tree in trees:
        taken += tree - height if tree - height > 0 else 0
    return taken


def binary_search(start, end, trees, target):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        taken = check(trees, mid)
        if taken >= target: # 적어도 M미터(traget) 이므로
            start = mid + 1 # 절단기의 높이를 늘려, 더 적은 크기의 나무를 가져오는 것
            result = mid
        else:
            end = mid - 1

    return result


def solution(n, m, trees):
    start, end = 0, max(trees)
    return binary_search(start, end, trees, m)


if __name__ == '__main__':
    N, M = map(int, input().split())
    li = [*map(int, sys.stdin.readline().split())]
    print(solution(N, M, li))
