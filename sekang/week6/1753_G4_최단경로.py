import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # cost, vertex
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
V, E = map(int, input().split()) # V : 1~20000
K = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)


for _ in range(E):
    u, v, w = map(int, input().split()) # u != v, w<=10
    graph[u].append((v, w))

dijkstra(K)

for dist in distance[1:V+1]:
    if dist == INF:
        print("INF")
    else:
        print(dist)