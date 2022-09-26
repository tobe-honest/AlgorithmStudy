import sys
from collections import defaultdict,deque
input=sys.stdin.readline
n=int(input())
m=int(input())

graph=defaultdict(list)
for i in range(n):
    tmp=list(map(int,input().split(' ')))
    for nn in range(n):
        if tmp[nn]:
            graph[i+1].append(nn+1)

plan=list(map(int,input().split(' ')))

def bfs(start,end):
    visited=[False]*(n+1) # 없으면 계속해서 돌기 때문에 visited가 꼭 필요하다
    visited[start]=True
    q=deque([start])

    while q:
        node=q.popleft()
        if node==end: # 종료조건
            return True

        for can in graph[node]: # 현재 여행지에서 갈 수 있는 곳들 q에 넣기
            if not visited[can]:
                q.append(can)
                visited[can]=True

    return False

flag=True
for i in range(m-1):
    if not bfs(plan[i],plan[i+1]): # 시작 도시 -> 도착 도시
        flag=False
        break

print('YES' if flag else 'NO')
