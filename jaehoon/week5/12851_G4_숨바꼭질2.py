from collections import deque

def check():
    global min_cnt
    global min_level
    queue = deque([[N,0]])
    visit = [False for i in range(100001)]

    while(queue):
        x,level = queue.popleft()
        visit[x] = True
        
        if level>min_level:
            continue

        if x==K:
            min_level = level
            min_cnt+=1
            continue
        
        kx1,kx2,kx3 = x-1,x+1,x*2
        if 0<= kx1 <= 100000 and visit[kx1] == False:
            queue.append([kx1,level+1])
        if 0<= kx2 <= 100000 and visit[kx2] == False:
            queue.append([kx2,level+1])
        if 0<= kx3 <= 100000 and visit[kx3] == False:
            queue.append([kx3,level+1])
   
N,K = map(int,input().split())
min_cnt, min_level = 0, 100000
check()
print(min_level)
print(min_cnt)