import sys
input=sys.stdin.readline
n,l=map(int,input().split(' '))
graph=list()
for _ in range(n):
    graph.append(list(map(int,input().split(' '))))

def check(graph):
    visited=[False]*n
    for i in range(n-1):
        if graph[i]==graph[i+1]: # 높이 같음
            continue
        if abs(graph[i]-graph[i+1])>1: # 높이가 2 이상 차이남
            return False
        if abs(graph[i]-graph[i+1])==1:
            if graph[i]>graph[i+1]: # 왼쪽위쪽이 높은 상황
                if i+1+l<=n: # 범위 내이면
                    compare=graph[i+1]
                    for j in range(i+1,i+l+1):
                        if compare!=graph[j] or visited[j]: # 높이가 중간에 달라지거나 이미 놓아져 있는 경우
                            return False
                    visited[i+1:i+l+1]=[True]*l # 놓았다고 처리
                else:
                    return False
            else: # 오른쪽 아래쪽이 높은 상황
                if i-(l-1)>=0:
                    compare=graph[i]
                    for j in range(i-(l-1),i+1):
                        if compare!=graph[j] or visited[j]:
                            return False
                    visited[i-(l-1):i]=[True]*l
                else:
                    return False
    return True
    
cnt=0
for i in range(n):
    # 가로
    now=list()
    now=graph[i][:]
    if check(now):
        cnt+=1
    # 세로
    now=list()
    for j in range(n):
        now.append(graph[j][i])
    if check(now):
        cnt+=1
print(cnt)
