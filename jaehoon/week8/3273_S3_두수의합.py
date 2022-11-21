import sys
N = int(input())
lst = list(map(int,sys.stdin.readline().split()))
x = int(input())

lst.sort()
start,end,cnt = 0,N-1,0

if N==1:
    print(0)
    exit()

while start<end:
    if lst[start] + lst[end] > x:
        end-=1
    elif lst[start] + lst[end] < x:
        start+=1
    elif lst[start] + lst[end] == x:
        start+=1
        end-=1
        cnt+=1
print(cnt)

