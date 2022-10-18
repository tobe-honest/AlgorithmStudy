import heapq
import sys

def dijkstra(S):
    queue = []
    heapq.heappush(queue, [0,S])
    distance[S] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distance[node] < dist:
            continue
        
        for adj_node in graph[node]:
            cost = distance[node] + adj_node[1]   
            if cost < distance[adj_node[0]]:     
                distance[adj_node[0]] = cost
                heapq.heappush(queue, (cost, adj_node[0]))

V, E = map(int,input().split())
S = int(input())
INF = int(1e9)

distance = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v, w))
    
dijkstra(S)

for i in range(1,len(distance)):
    if i==S:
        print(0)
    elif distance[i] == INF:
        print("INF",end="\n")
    else:
        print(distance[i])