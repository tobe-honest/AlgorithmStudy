import sys
N,K = map(int,input().split())
lst = list(map(int,input().split()))

std = max = sum(lst[0:K])
start,end = 0,K-1

for i in range(0,N-K):
    std = std - lst[start] + lst[end+1]
    start +=1
    end +=1
    if max < std:
        max = std

print(max)
