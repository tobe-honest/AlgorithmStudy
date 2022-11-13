import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    nums=list()
    for _ in range(n):
        nums.append(input().rstrip())
    nums.sort()
    answer='YES'
    flag=False
    for i in range(len(nums)-1):
        if nums[i+1][:len(nums[i])]==nums[i]:
            flag=True
            answer='NO'
            break
    print(answer)