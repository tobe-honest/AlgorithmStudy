import sys
input = sys.stdin.readline

def binary_search(trees, left, right):
    res = 0
    while left <= right:
        length = 0
        mid = (left + right) // 2
        length = sum([trees[i]-mid if trees[i]-mid > 0 else 0 for i in range(N)])
        if length == M:
            print(mid)
            return
        elif length >= M:
            left = mid + 1
            res = mid
        elif length < M:
            right = mid - 1
    print(res)
    return

# N : 나무의 수, M : 나무의 길이
N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
binary_search(trees, 0, trees[-1])