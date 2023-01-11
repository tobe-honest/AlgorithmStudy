import sys

n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for i in range(q):
    t,k = map(int,sys.stdin.readline().split())
    if t == 1:
        if (len(tree[k]) < 2):
            print("no")
        else:
            print("yes")

    elif t == 2:
        print("yes")