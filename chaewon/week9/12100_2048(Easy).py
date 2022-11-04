n=int(input())
graph=list()
for _ in range(n):
    graph.append(list(map(int, input().split(' '))))
print(graph)

def move_right(graph): # 개 거지같이 짜버렸다;;
    for i in range(n):
        j=n-1
        while j>=0:
            if j==0: # 홀수
                break
            if graph[i][j] == graph[i][j-1]:
                graph[i][j]*=2
                graph[i][j-1]=0
                j-=2
            else:
                j-=1

    for j in range(n):
        cnt=0
        while 0 in graph[j]:
            graph[j].remove(0)
            cnt+=1
        graph[j]=[0]*cnt+graph[j]
    return graph
# print(move_right(graph))
def move_left(graph):
    for i in range(n):
        while j<n:
            if i==n-1: # 홀수
                break
            if graph[j][i] == graph[j][i+1]:
                graph[j][i]*=2
                graph[j][i+1]=0

    for j in range(n):
        cnt=0
        while 0 in graph[j]:
            graph[j].remove(0)
            cnt+=1
        graph[j]=graph[j]+[0]*cnt
    return graph
print(move_left(graph))
def move_up(graph):
    result=[[] for _ in range(n)]
    for i in range(n):
        for j in range(0,n,2):
            if j==n-1: # 홀수
                break
            if graph[j][i] == graph[j+1][i]:
                result[i].append(graph[j][i]*2)
                graph[j+1][i]=0
            else:
                result[i].append(graph[j][i])
    print('result',result)
    for i in range(n):
        cnt=0
        for j in range(n):           
            if cnt>=len(result):
                graph[j][i]=0
            else:
                graph[j][i]=result[j]
                cnt+=1    
    print(graph)
# move_up(graph)