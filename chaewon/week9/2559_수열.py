from collections import deque
n,k=map(int, input().split(' '))
seq=list(map(int, input().split(' ')))

now=deque(seq[:k])
now_sum=sum(now)
max_value=sum(now)

for i in range(k,len(seq)):
    # print(now)
    minus=now.popleft()
    now_sum-=minus
    now.append(seq[i])
    # print(now)
    now_sum+=seq[i]
    max_value=max(now_sum, max_value)
    # print('------',max_value)
print(max_value)