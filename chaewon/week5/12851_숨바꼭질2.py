import sys
from collections import defaultdict,deque
input=sys.stdin.readline
n,k=map(int,input().split(' '))

q=deque([[n,0]]) # [시작 위치, 시간]
visited=[100001]*100001 #수빈이가 0부터 시작하고 모든 칸 걸으면 가장 오래걸리는 시간은 100001일 것이다
visited[n]=0 # 시작 위치에서 시간 처리
answers=list()

while q:
    now,time=q.popleft()
    if now==k: # 잡았다..!
        answers.append(time)

    if now-1>=0 and now-1<=100000 and visited[now-1]>=time+1: # 왼쪽으로 걷기
        q.append([now-1,time+1])
        visited[now-1]=time+1
    if now+1>=0 and now+1<=100000 and visited[now+1]>=time+1: # 오른쪽으로 걷기
        q.append([now+1,time+1])
        visited[now+1]=time+1
    if now*2>=0 and now*2<=100000 and visited[now*2]>=time+1: # 순간이동
        q.append([now*2,time+1])
        visited[now*2]=time+1

print(answers[0]) # 어차피 answers에는 도착한 모든 것이 들어가는 것이 아니라 최소 시간으로 도착한 것만 들어가게 된다
print(len(answers))
