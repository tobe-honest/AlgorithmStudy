import sys
from collections import deque
input=sys.stdin.readline
s=int(input())

graph=[[-1]*(s+1) for _ in range(s+1)] # [현재 입력][copied]
graph[1][0]=0
def bfs(now,copied):
    q=deque([[now,copied]])
    while q:
        now,copied=q.popleft()

        # 복사 
        if graph[now][now]==-1:
            graph[now][now]=graph[now][copied]+1
            q.append([now,now])
        # 삭제
        next=now-1
        if 0<next<=s and graph[next][copied]==-1:
            graph[next][copied]=graph[now][copied]+1
            q.append([next,copied])

        # 붙여넣기
        next=now+copied
        if next<=s and graph[next][copied]==-1 :
            graph[next][copied]=graph[now][copied]+1
            q.append([next,copied])

bfs(1,0)

answer=graph[s][1]
for i in range(2,s):
    if graph[s][i]!=-1:
        answer=min(answer, graph[s][i])
print(answer)
