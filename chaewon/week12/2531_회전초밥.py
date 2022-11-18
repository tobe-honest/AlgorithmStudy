from collections import defaultdict
import sys
input=sys.stdin.readline
n,d,k,c=map(int,input().split(' '))
sushi=list()
for i in range(n):
    sushi.append(int(input()))

sushi=sushi+sushi[:k-1] # 필요한 만큼 앞의 초밥을 떼서 연결
now=sushi[:k-1]
max_val=0
sushi_dict=defaultdict(int)
sushi_set=set(now)

sushi_set.add(c)
sushi_dict[c]+=1
for su in now:
    sushi_dict[su]+=1

for i in range(k-1,len(sushi)):
    now.append(sushi[i])
    sushi_set.add(sushi[i])
    sushi_dict[sushi[i]]+=1
    eat=now[0]
    now=now[1:]

    if len(sushi_set)>max_val:
        max_val=len(sushi_set)

    sushi_dict[eat]-=1
    if sushi_dict[eat]==0:
        sushi_set.remove(eat)
print(max_val)