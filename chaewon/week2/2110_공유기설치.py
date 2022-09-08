import sys

n,c=map(int,sys.stdin.readline().split(' '))
home=list()
for _ in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()

def if_possible(mid):
    pointer=0
    router=1 # 맨 처음 공유기 설치
    for i in range(n):
        if home[i]-home[pointer]>=mid:
            pointer=i
            router+=1

    if router<c:
        return False
    return True

lo=0
hi=home[len(home)-1]-home[0]
answer=0
while lo<=hi:

    mid=(lo+hi)//2

    if if_possible(mid):
        answer=mid
        lo=mid+1
    else:
        hi=mid-1

print(answer)
