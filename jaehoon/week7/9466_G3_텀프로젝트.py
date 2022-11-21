import sys
sys.setrecursionlimit(1000000)

def check(v):
    global cnt

    visit[v] = True
    next = lst[v]

    if not visit[next]:
        check(next)
    elif not end[next]:
        temp=next
        while(1):
            temp=lst[temp]
            cnt+=1
            if temp==next:
                break
    end[v]=1

T = int(input())

for t in range(T):
    N = int(input())
    lst = [0] + list(map(int,input().split()))
    visit = [False for j in range(N+1)]
    end = [False for j in range(N+1)]
    cnt=0
    for i in range(1,N+1):
        if visit[i] == False:
            check(i)
    print(N-cnt)