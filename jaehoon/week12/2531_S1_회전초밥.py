n,d,k,c = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

result = 0
count = [0] * d
cnt= 0
v = []
for i in range(len(lst)+k):
    idx = i%len(lst)

    if len(v) < k:
        v.append(lst[idx])
        count[lst[idx]-1]+=1
    
    elif len(v) == k:
        val = v.pop(0)
        v.append(lst[idx])
        count[val-1]-=1
        count[lst[idx]-1]+=1
    
    if count[c-1] == 0:
        result = max(result,d-count.count(0)+1)
    else:
        result = max(result,d-count.count(0))


print(result)