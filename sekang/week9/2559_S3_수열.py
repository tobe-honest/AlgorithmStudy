import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, K = map(int, input().split()) # 전체 날짜 수, 연속적인 날짜 수
    temp = list(map(int, input().split()))

    # 부분 합
    for i in range(1, N):
        temp[i] = temp[i] + temp[i-1]
    
    # print(temp)
    res = temp[K-1]
    j = 0
    for i in range(K, N):
        if temp[i] - temp[j] > res:
            res = temp[i] - temp[j]
        j += 1
    
    print(res)

    # 0 1  2   3   4  5  6  7  8  9 : index 
    # 3 1 -3 -12 -12 -9 -2 11 19 16