import sys
import heapq
input=sys.stdin.readline
v,e =map(int,input().split(' '))
k=int(input())
INF=int(1e9)
graph=[{} for x in range(v+1)]

for i in range(e):
    start,end,cost=map(int,input().split(' '))
    if end in graph[start].keys():
        graph[start][end]=min(graph[start][end],cost)
    else:
        graph[start][end]=cost
distance=[INF]*(v+1)

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for end_node in graph[now].keys():
            cost=dist+graph[now][end_node]
            if cost<distance[end_node]:
                distance[end_node]=cost
                heapq.heappush(q, (cost, end_node))
dijkstra(k)
for i in range(1,v+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])
