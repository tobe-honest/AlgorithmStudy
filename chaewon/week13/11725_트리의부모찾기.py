from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
n=int(input())

tree=defaultdict(list)
for _ in range(n-1):
    a,b=map(int,input().split(' '))
    tree[a].append(b)
    tree[b].append(a)
    
visited=[0]*(n+1)

def find_child(now):
    
    if now in tree.keys():
        child=tree.pop(now)
    else:
        return
    for c in child:
        if visited[c]==0:
            visited[c]=now
            find_child(c)
find_child(1)
for i in range(2,len(visited)):
    print(visited[i])