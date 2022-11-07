import sys
sys.setrecursionlimit(100000)
n=int(input())
graph=[[]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    start, end, cost= map(int, input().split(' '))
    graph[start].append([end,cost])
    graph[end].append([start,cost])

def dfs(graph, v, visited):
    for next_node, cost in graph[v]:
        if visited[next_node]<0:
            visited[next_node]=visited[v]+cost
            dfs(graph, next_node, visited)

    return visited
visited=[-1]*(n+1)
visited[1]=0
visited=dfs(graph,1,visited)
a=visited.index(max(visited))

visited=[-1]*(n+1)
visited[a]=0
visited=dfs(graph,a,visited)
print(max(visited))