import sys

n,s = map(int,input().split())
lst = list(map(int,sys.stdin.readline().split()))

left,right = 0,0
result = 1e9
val = 0

while True:
    if val >= s:
        result = min(result,right-left)
        val -= lst[left]
        left += 1
    
    else:
        if right == n:
            break
        
        val += lst[right]
        right +=1


if result == 1e9:
    print(0)
else:
    print(result)