# 시간초과
n=int(input())
cnt=0

def is_possible(location):
    graph=[[False]*n for _ in range(n)]
    for x,y in enumerate(location):
        if graph[x][y]==False:
            graph[x]=[True]*n # 가로 
            # 세로
            for i in range(n):
                graph[i][y]=True

            # 오른 밑 대각선
            for i,j in zip(range(x+1,n),range(y+1,n)):
                graph[i][j]=True

            # 왼 위 대각선
            for i,j in zip(range(0,x),range(0,y)):
                graph[i][j]=True

            # 오른 위 대각선
            for i,j in zip(range(x-1,-1,-1),range(y+1,n)):
                graph[i][j]=True

            # 왼 아래 대각선
            for i,j in zip(range(x+1,n),range(y-1,-1,-1)):
                graph[i][j]=True
        else:
            return False

    return True

def recursive(location):
    global cnt
    for i in range(n):
        if i in location:
            continue
        location.append(i)
        if is_possible(location):
            if len(location)==n:
                cnt+=1    
        else:
            location.pop()
            continue
        recursive(location)
        location.pop()
recursive([])
print(cnt)