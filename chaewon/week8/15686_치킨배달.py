import sys
from itertools import combinations
input=sys.stdin.readline
n,m =map(int, input().split(' '))

graph=list()
home=list()
chicken=list()
for i in range(n):
    tmp=list(map(int, input().split(' ')))
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j]==1: #home
            home.append([i,j])
        elif tmp[j]==2: # chicken
            chicken.append([i,j])

distance=list()
for h in home:
    home_x, home_y=h
    tmp=[]
    for c in chicken:
        chicken_x, chicken_y=c
        tmp.append(abs(chicken_x-home_x)+abs(chicken_y-home_y))
    distance.append(tmp)

chicken_distance=list()
can=list(combinations(range(len(chicken)), m)) #[(0,1,2),(0,3,4)] # 남길 치킨집
mins=list()
for c in can:# c=(0,3,4)
    city=0
    for i in range(len(home)):
        min_per_home=int(1e9)
        # print('c',c)
        for cc in c:
            min_per_home=min(min_per_home,distance[i][cc])
        city+=min_per_home
    mins.append(city)
print(min(mins))
