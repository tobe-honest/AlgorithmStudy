import sys
input = sys.stdin.readline

def search(A, B):
    cnt = 0
    for i in range(N_A):
        target = A[i]
        left = 0
        right = N_B-1
        if target > B[right]:
            cnt += N_B
            continue
        if target == 1: continue

        while left <= right:
            mid = (left+right) // 2
            ## 크기가 작은 것만 되기 때문에 크기가 같으면 right를 옮겨줌
            if B[mid] >= target:
                right = mid-1
            else:
                left = mid+1
        ## right가 멈춘 인덱스 부터 0까지가 가능한 원소들
        ## 인덱스는 0부터 시작이니까 +1 해줌
        cnt += right + 1
    return cnt
T = int(input())
for _ in range(T):
    N_A, N_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()
    print(search(A, B))