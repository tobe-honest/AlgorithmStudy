import sys

n,d,k,c = map(int,sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for _ in range(n)]

result = 0
count = [0] * d
uni = set()

for i in range(n+k):
    idx = i%n

    if idx < k:
        count[lst[idx]-1]+=1
        uni.add(lst[idx])
    
    else:
        count[lst[idx-k]-1]-=1
        if count[lst[idx-k]-1] == 0:
            uni.remove(lst[idx-k])
        count[lst[idx]-1]+=1
        uni.add(lst[idx])
    
        if count[c-1] == 0:
            result = max(result,len(uni)+1)
        else:
            result = max(result,len(uni))

print(result)