n= int(input())
budgets=list(map(int,input().split(' ')))
total=int(input())

def is_possible(mid):
    tmp=0
    for budget in budgets:
        if budget >mid:
            tmp+=mid
        else:
            tmp+=budget
    if tmp>total:
        return False
    else: 
        return True

answer=max(budgets)
if sum(budgets)>total:
    start=0
    end=max(budgets)
    
    while start<=end:
        mid=(start+end)//2
        
        if is_possible(mid):
            start=mid+1
            answer=mid
        else:
            end=mid-1
print(answer)