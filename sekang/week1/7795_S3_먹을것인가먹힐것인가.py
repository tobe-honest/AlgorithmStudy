import sys
input=sys.stdin.readline
def binary_search(idx, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 비교하는 값이 범위 중간 값보다 큰 경우
        if b[mid] < a[idx]:
            start = mid + 1
        # 더 작은 경우 = 끝 범위를 줄여야 하는 경우
        else:
            end = mid - 1
    return start

t = int(input())
result = []

for _ in range(t):
    total = 0
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()

    for i in range(n):
        total += binary_search(i, 0, m-1)

    result.append(total)

for res in result:
    print(res)