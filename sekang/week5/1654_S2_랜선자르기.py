def binary_search(length, left, right):
    res = 0
    while left <= right:
        cnt = 0
        mid = (left + right) // 2
        cnt = sum([length[k] // mid for k in range(K)])

        if cnt >= N: # 개수 줄여야 함 = mid 늘리기
            res = mid
            left = mid + 1
        else: # 개수 줄여야 함 = mid 줄이기
            right = mid - 1
    print(res) # 출력 : 랜선의 최대 길이(정수)
    return

K, N = map(int, input().split()) # 현재 랜선의 개수, 필요한 랜선의 개수
length = [int(input()) for _ in range(K)]
binary_search(length, 1, max(length))
