n,m =map(int,input().split(' '))

seq=list(map(int,input().split(' ')))
# 구간의 점수의 최댓값(value)의 최솟값을 구하는 프로그램

def is_possible(mid):
    partition=[0]
    start=0
    now=1
    while now<=n:
        part=seq[start:now] # 대상 구간
        if max(part)-min(part)> mid: # 전에 끊기
            partition.append(now-1)
            start=now-1
            now=start+1
        else:
            now+=1
    if partition[-1]!=n:
        partition.append(n)

    if len(partition)-1>m :
        return False
    elif len(partition)-1<=m :
        return True

low=0
high=max(seq)
result=low
while low<=high:
    mid=(low+high)//2

    if is_possible(mid): # 작아짐
        result=mid
        high=mid-1
    else: # 커져야함
        low=mid+1
print(result)
