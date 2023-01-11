import sys
input=sys.stdin.readline
n,m=map(int,input().split(' ')) # 입국심사대 n개 ,친구 m 명
times=[]
for i in range(n):
    times.append(int(input()))
start=0
end=max(times)*m

def is_possible(mid):
    count=0
    for t in times:
        count+=mid//t
    if count>= m:
        return True
    else:
        return False

while start<=end:
    mid=(start+end)//2

    if is_possible(mid):
        answer=mid
        end=mid-1
    else:
        start=mid+1
print(answer)