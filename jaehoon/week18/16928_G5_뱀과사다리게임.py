from collections import deque

def check():
    queue = deque([[1,0]])
    visit = [False] * 101

    while queue:
        x,level = queue.popleft()
        visit[x] = True
        if x >= 100:
            print(level)
            return

        for i in range(1,7):
            kx = x + i
            if kx > 100 or visit[kx] == True:
                continue

            for i in snake:
                if i[0] == kx:
                    kx = i[1]
            for i in ladder:
                if i[0] == kx:
                    kx = i[1]
            
            queue.append([kx,level+1])
            visit[kx] = True

n,m = map(int,input().split())

snake,ladder = [],[]

for _ in range(n):
    x,y = map(int,input().split())
    ladder.append([x,y])

for _ in range(m):
    u,v = map(int,input().split())
    snake.append([u,v])

check()