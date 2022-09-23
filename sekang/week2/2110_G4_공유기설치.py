import sys
input = sys.stdin.readline

def binary_search(start, end):
    result = 0

    while start <= end: 
        mid = (start + end) // 2
        idx = 0
        cnt = 1    

        # 처음에 공유기를 설치하고 특정 길이 이상이 되면 공유기 설치
        for i in range(n):
            if (x[i] - x[idx]) >= mid:
                idx = i
                cnt += 1
        
        # 설치된 공유기 수에 따라 거리 조절
        if cnt < c: # 거리가 짧아져야 함
            end = mid - 1
        else: # 거리가 길어져야 함
            start = mid + 1
            result = mid

    print(result)
    return

n, c = map(int, input().split())
x = sorted([int(input().rstrip()) for _ in range(n)])

binary_search(1, x[-1]-x[0])