import sys

def check():
    start,end = 0,lst[-1]

    while start<=end:
        mid = (start+end)//2
        cum = 0
        for val in lst:
            if val <= mid:
                cum+= val
            elif val > mid:
                cum += mid
        
        if cum == limit:
            print(mid)
            return

        if cum < limit:
            start = mid+1
        elif cum > limit:
            end = mid-1
    
    print((start+end)//2)
    return
    

n = int(input())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort()
limit = int(input())

if sum(lst) <= limit:
    print(max(lst))
else:
    check()