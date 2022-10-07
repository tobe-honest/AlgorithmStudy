import sys
input=sys.stdin.readline
n,m,l=map(int,input().rstrip().split(' '))
rest=[l] # 맨 마지막 길이까지 고려해야 함
if n!=0: # n=0일때 입력이 개행만 들어오는 것 처리 -> 런타임에러(Value Error)의 원인
    x=list(map(int,input().rstrip().split(' ')))
    rest=rest+x
rest.sort()

low=1
high=l-1 # 맨 끝에는 휴게소를 세울 수 없음
result=0
def is_possible(mid):
    now=0
    new_rest=list() # 휴게소를 새로 짓게될 위치
    for r in rest:
        while (r-now)>mid: # 간격이 mid보다 크면
            now+=mid # 이 위치에
            new_rest.append(now) # 짓는다
        now=r # now 갱신

    if len(new_rest)>m: # 현재 mid길이가 길어서 휴게소를 덜 세움-> mid 줄이기
        return False
    return True
    
while low<=high:
    mid=(low+high)//2
    if is_possible(mid):
        high=mid-1
        result=mid
    else:
        low=mid+1
print(result)
