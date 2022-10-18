
def check():
    start,end = 1, L-1
    while start<=end:
        cnt, mid = 0, (start+end) // 2
        for i in range(1, len(lst)):
            if lst[i] - lst[i-1] >= mid:
                cnt += (lst[i]-lst[i-1]-1)//mid
        if cnt > M:
            start = mid + 1
        else:
            end = mid-1

    print((start+end)//2+1)
    
N,M,L = map(int,input().split())
lst = [0] + list(map(int,input().split())) + [L]
lst.sort()
check()
