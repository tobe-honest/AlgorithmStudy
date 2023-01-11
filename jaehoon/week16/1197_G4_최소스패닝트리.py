import sys

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


def union(pa, pb):
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

v, e = map(int, sys.stdin.readline().split())
parent = [x for x in range(v+1)]
edges = []

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

result = 0
edges.sort(key=lambda x: x[2])

for edge in edges:
    a, b, c = edge[0], edge[1], edge[2]
    pa,pb = find_parent(a),find_parent(b)
    if pa!=pb:
        union(pa, pb)
        result += c

print(result)