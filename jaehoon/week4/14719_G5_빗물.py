H, W = map(int,input().split())
lst = list(map(int,input().split()))

total = 0
for i in range(1,len(lst)):
    left = max(lst[:i])
    right = max(lst[i:])
    stand = min(left,right)
    if stand > lst[i]:
        total = total + (stand-lst[i])

print(total)
    
        
