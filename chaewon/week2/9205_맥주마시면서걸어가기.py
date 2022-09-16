from collections import deque
t=int(input())

def bfs(conv,visited):
    q=deque([[home_x,home_y]])
    visited[(home_x,home_y)]=True
    while q:
        x,y=q.popleft()

        if x==fest_x and y==fest_y:
            print('happy')
            return

        for store_x,store_y in conv:
            if abs(store_x-x)+abs(store_y-y)<=1000 and visited[(store_x,store_y)]==False:
                q.append([store_x,store_y])
                visited[(store_x,store_y)]=True
    print('sad')

for _ in range(t):
    n=int(input()) # 편의점 수
    home_x,home_y=map(int,input().split(' '))
    conv=list()
    visited=dict()
    for _ in range(n):
        tmp=list(map(int,input().split(' ')))
        conv.append(tmp)
        visited[tuple(tmp)]=False

    fest_x,fest_y=map(int,input().split(' ')) # 페스티벌 위치
    conv.append([fest_x,fest_y])
    visited[(fest_x,fest_y)]=False

    bfs(conv,visited)
