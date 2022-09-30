

N = int(input())
lst = list(map(int,input().split()))

result = 0
cnt=0
temp=0
for i in range(N):
    if lst[i]<0:
        cnt+=1

if cnt==N:
    print(max(lst))
    exit(0)

for i in range(N):    
    result = result + lst[i]
    if result<0:
        result=0
    
    if temp < result:
        temp = result

print(temp)