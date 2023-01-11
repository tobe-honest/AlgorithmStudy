from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
tree=defaultdict(list)

for i in range(n-1):
    a=list(map(int,input().split(' ')))
    tree[a[0]].append(a[1])
    tree[a[1]].append(a[0])

depth=[1]*(n+1)
q=deque([[1,1]])
visited=[False]*(n+1)
visited[1]=True
while q:
    node,d=q.popleft()
    depth[node]=d
    for n in tree[node]:
        if not visited[n]:
            q.append([n,d+1])
            visited[n]=True

def find_parent(one,other):
    # depth 맞춰주기
    if depth[one] != depth[other]:
        if depth[one]>depth[other]:
            big,small=one,other
        else:
            big,small=other,one
        now_depth=depth[big]

        while now_depth!=depth[small]:
            for n in tree[big]:
                if depth[n]<now_depth:
                    big=n
                    now_depth=depth[n]
                    break
    else:
        big=one
        small=other
    while big!=small:
        for n in tree[big]:
            if depth[n]<depth[big]:
                big=n
                break
        for n in tree[small]:
            if depth[n]<depth[small]:
                small=n
                break
    return small
m=int(input())
for i in range(m):
    a=list(map(int,input().split(' ')))
    print(find_parent(a[0],a[1]))