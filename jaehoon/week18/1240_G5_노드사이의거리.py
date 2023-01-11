import sys

def dfs(start, target,cost):
    visit[start] = True

    if start == target:
        print(cost)
        return

    for val in tree[start]:
        if visit[val[0]] == False:
            dfs(val[0],target,cost+val[1])

n,m = map(int,input().split())
tree = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int,sys.stdin.readline().split())
    tree[a].append([b,c])
    tree[b].append([a,c])

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    visit = [False] * (n+1)
    dfs(a,b,0)