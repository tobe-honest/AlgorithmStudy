import sys
input = sys.stdin.readline

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        minimum, maximum = l[0], l[0]
        for i in range(N):
            if l[i] > maximum : maximum = l[i]
            if l[i] < minimum : minimum = l[i]
            if maximum - minimum > mid:
                cnt += 1        
                minimum, maximum = l[i], l[i]
        if cnt > M:
            start = mid + 1
        else:  
            result = mid
            end = mid - 1

    return result

N, M = map(int, input().split())
l = list(map(int, input().split()))
print(binary_search(0, max(l)-min(l)))