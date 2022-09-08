def check(x,level):
    global flag
    visited[x] = True
    if x == end:
        print(level)
        flag=1
        return

    for i in range(len(tree[x])):
        if visited[tree[x][i]] == False:
            check(tree[x][i],level+1)

N=int(input())
start,end=map(int,input().split())
M=int(input())
tree=[[] for i in range(N+1)]
visited=[False for i in range(N+1)]
flag=0
for i in range(M):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
check(start,0)

if flag==0:
    print(-1)