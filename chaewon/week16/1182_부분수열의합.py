# 순열 # 맞음
n,s=map(int, input().split(' '))
seq=list(map(int, input().split(' ')))

from itertools import combinations
answer=0

for length in range(1,n+1):
    comb = list(combinations(seq,length))
    for c in comb:
        if sum(c)==s:
            answer+=1

print(answer)

# 백트래킹 # 시간초과
import sys
input=sys.stdin.readline
n,s=map(int, input().split(' '))
seq=list(map(int, input().split(' ')))
answer=0
comb=list()
def ncr(now,arr,r,visited):
    global answer
    if len(now)==r and sum(now)==s:
        answer+=1
        return
    
    now_visited=visited[:]
    for i in range(n):
        if not now_visited[i]:
            now_visited[i]=True
            now.append(arr[i])
            ncr(now,arr,r,now_visited)
            now.pop()

visited=[False]*n
for length in range(1,n+1):
    ncr([],seq,length,visited)

print(answer)