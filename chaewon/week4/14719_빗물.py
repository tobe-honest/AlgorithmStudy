import sys
input=sys.stdin.readline

h, w= map(int, input().split(' '))
heights=list(map(int, input().split(' ')))

graph=[ [0]* h for _ in range(w)]
for i, height in enumerate(heights):
    for j in range(height):
        graph[i][j]=1

water=0
for i in range(h):
    flag=False
    for j in range(w):
        if graph[j][i] and flag==False : # 막힘
            flag=True # 세기 시작
            cnt=0

        if graph[j][i] and flag==True: # 세기 끝
            water+=cnt
            cnt=0

        if graph[j][i]==0 and flag==True:
            cnt+=1
print(water)
