def binary_search(data, left, right, N, M):
    result = 0
    while left <= right:
        cnt = 1
        idx = 0
        mid = (left + right) // 2 # mid 값과 cnt 개수는 반비례

        for i in range(N):
            part = data[idx:i+1]
            score = max(part) - min(part)
            if score > mid:
                idx = i
                cnt += 1

        if cnt > M: # 구간을 개수를 줄여야 하는 경우
            left = mid + 1
            
        else: # 구간을 늘리거나 기억할 필요가 있는 경우
            right = mid - 1
            result = mid

    print(result)
    return

N, M = map(int, input().split()) # 입력 2개로 받는거에서 자꾸 실수하네?
data = list(map(int, input().split()))
# 구간의 점수 : [0, Max-MIN]
binary_search(data, 0, max(data) - min(data), N, M)