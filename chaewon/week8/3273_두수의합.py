import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split(' ')))
x=int(input())

arr.sort()
right=n-1
cnt=0
flag=True

for left in range(n):
    if left>=right:
        break
    while arr[right]+arr[left] >=x and right>=0:
        if arr[right]+arr[left] ==x:
            right-=1
            cnt+=1
            break
        elif arr[right]+arr[left] >x:
            right-=1

        if left>=right:
            flag=False
            break
    if flag==False:
        break
print(cnt)