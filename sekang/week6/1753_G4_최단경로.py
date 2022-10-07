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


# 현재 노드가 이미 처리된 적 있는 노드라면 무시할 수 있는 이유
# -> 기본적으로 거리가 짧은 원소가 우선순위 큐의 최상위 원소로 위치해서
# 꺼낼 때, 이미 전에 처리하면서 해당 노드에서 나가는 간선을 모두 처리했기 때문

# 우선순위 큐에서 거리가 짧은 원소들이 먼저 나오기 때문에 최소 거리를 보장