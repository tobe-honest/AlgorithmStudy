import sys
from collections import defaultdict,deque
input=sys.stdin.readline
n=int(input()) # 도시의 갯수
m=int(input()) # 버스의 갯수
bus=[[int(1e9)]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            bus[i][j]=0
for _ in range(m):
    start, end, cost=map(int,input().split(' '))
    if cost<=bus[start][end]:
        bus[start][end]=cost
for k in range(n+1): # 거쳐가는 노드
    for i in range(n+1): # 시작 도시
        for j in range(n+1): # 도착 도시
            bus[i][j]=min(bus[i][k] + bus[k][j],bus[i][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j]==int(1e9):
            print('0', end=' ')
        else:
            print(bus[i][j],end=' ')
    print('')
