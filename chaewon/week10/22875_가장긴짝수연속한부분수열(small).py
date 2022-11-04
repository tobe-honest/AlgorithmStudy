from collections import deque
n,k=map(int,input().split(' '))
seq=list(map(int, input().split(' ')))

od=[seq[i]%2 for i in range(n)]
od+=[1]
values,maxes=deque([]),list() # 삭제한 index
now=0
for i in range(0,n+1):
    if od[i]==0: # 짝수이면
        now+=1
    if od[i]==1: # 홀수를 삭제
        values.append(now)
        maxes.append(sum(values))
        now=0
        if len(values)==k+1:
            maxes.append(sum(values))
            values.popleft()

if len(maxes)==0:
    print(0)
else:
    print(max(maxes))