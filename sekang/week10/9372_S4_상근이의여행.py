import sys
input = sys.stdin.readline

def dfs(node, cnt):
    visited[node] = True
    for no in graph[node]:
        if not visited[no]:
            cnt = dfs(no, cnt+1)
    return cnt

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]

        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n+1)
        cnt = dfs(1, 0)
        print(cnt)