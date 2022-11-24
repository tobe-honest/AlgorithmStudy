import sys
from collections import deque

def solution(tree,n):
    queue = deque([1])
    p = [0] * (n+1)

    while queue:
        now = queue.popleft()
        for node in tree[now]:
            if node != 1 and p[node] == 0:
                p[node] = now
                queue.append(node)
    
    for i in range(2,n+1):
        print(p[i])


if __name__ == "__main__":
    n = int(input())
    tree = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        tree[a].append(b)
        tree[b].append(a)

    solution(tree,n)