# 구간의 점수 = MAX_구간값 - MIN_구간값
# 구간의 점수의 최대값 중 최솟값을 구하라
# 접근 1) 이분탐색을 점수를 기준으로 탐색
# left = 1, right = 구간의 점수로 설정 후, 앞에서 부터 더하면서 구간의 점수가 mid보다 작아지면
# cnt +=1 하면서 마지막에 cnt(구간의 수)가 많으면 mid 줄이고 크면 좁힘, 같은 경우는 어디에 해야할까?

# 구간의 개수(M)를 right로 설정하면 아래 부분에서 부분합으로 비교하는게 이상해짐

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