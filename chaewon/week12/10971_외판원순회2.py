import sys
input=sys.stdin.readline
n=int(input())
w=list()
for i in range(n):
    w.append(list(map(int,input().split(' '))))

visited=[False]*n
global answer
answer=1e9
arr=[]
def tsp(cost):
    global answer
    if len(arr)==n:
        if w[arr[-1]][arr[0]]>0:
            cost+=w[arr[-1]][arr[0]]
            answer=min(answer,cost)
        return

    if cost>answer:
        return
    for i in range(n):
        if not visited[i]:
            if len(arr)==0:
                visited[i]=True
                arr.append(i)
                tsp(cost)
                visited[i]=False
                arr.pop()
            elif w[arr[-1]][i]>0:
                x=cost+w[arr[-1]][i]
                visited[i]=True
                arr.append(i)
                tsp(x)
                visited[i]=False
                arr.pop()
tsp(0)
print(answer)