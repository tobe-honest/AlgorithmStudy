import sys

n,m = map(int,sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for i in range(n)]
start,end = 0,lst[-1]*m

while start<=end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt = cnt + mid//lst[i]
        if cnt >= m:
            break
    
    if cnt >= m:
        end = mid-1
    elif cnt < m:
        start = mid+1

print(end+1)

