def check(start,end):
    while start<=end:
        mid = (start+end) // 2
        cnt=0
        for cable in lst:
            if mid==0: mid = 1
            cnt = cnt + cable//mid

        if cnt >= N:
            start = mid+1
        elif cnt<N:
            end = mid-1

    return end

K,N = map(int,input().split())
lst = []
for i in range(K):
    lst.append(int(input()))

lst.sort()

print(check(0,lst[-1]))