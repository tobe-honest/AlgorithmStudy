from collections import defaultdict
n,m=list(map(int,input().split(' ')))

tree=defaultdict(list)
for _ in range(n-1):
    s,e,distance=list(map(int,input().split(' ')))
    tree[s].append((e,distance))
    tree[e].append((s,distance))

def measure(s,e,visited,prev_dist):
    for node,dist in tree[s]:
        if visited[node]==0:
            visited[node]=prev_dist+dist
            measure(node,e,visited,visited[node])
    
for _ in range(m):
    s,e=list(map(int,input().split(' ')))
    visited=[0]*(n+1)
    visited[0],visited[s]=-1,-1
    measure(s,e,visited,0)
    print(visited[e])