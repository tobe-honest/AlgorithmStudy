import sys
sys.setrecursionlimit(10**9)

def dfs(x, w):
    for node in tree[x]:
        y, v = node
        if distance[y] == -1:
            distance[y] = w + v
            dfs(y, w + v)

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N-1):
    x, y, v = map(int, sys.stdin.readline().split())
    tree[x].append([y, v])
    tree[y].append([x, v])

distance = [-1] * (N + 1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
dfs(start, 0)
print(max(distance))