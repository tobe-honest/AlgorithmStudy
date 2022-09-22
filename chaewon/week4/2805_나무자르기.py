n,m=map(int,input().split(' '))
tree=(list(map(int,input().split(' '))))

low=0
high=max(tree)

def is_possible(mid):
    now=0
    for t in tree:
        if t>mid:
            now=now+t-mid

        if now>=m:
            return True

    return False

while low<=high:
    mid=(low+high)//2

    if is_possible(mid):
        # high=mid-1
        low=mid+1
        result=mid
    else:
        # low=mid+1
        high=mid-1
print(result)
