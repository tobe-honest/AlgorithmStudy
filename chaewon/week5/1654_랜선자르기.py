import sys
input=sys.stdin.readline
n,k=map(int,input().split(' '))
line=list()
for _ in range(n):
    line.append(int(input()))

def is_possible(mid):
    cnt=0
    for l in line:
        cnt=cnt+ (l//mid) # 해당 랜선에서 몇 도막까지 가져갈 수 있는지

    return True if cnt>=k else False

lo=1 # 가장 작은 길이가 0이 될 수 없음 -> zero division error
hi=max(line)
while lo<=hi:
    mid=(lo+hi)//2

    if is_possible(mid): # 최대 길이를 원하기 때문에 low값을 올려주는 방향
        lo=mid+1
        result=mid
    else:
        hi=mid-1
print(result)
