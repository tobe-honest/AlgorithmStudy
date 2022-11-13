from itertools import combinations
n=int(input())
seq=input()
alpha=set(seq)
candidate=list(combinations(alpha,n))
answer=0
for can in candidate:
    cnt=0
    for i in range(len(seq)):
        if seq[i] in can:
            cnt+=1
        else:
            answer=max(answer,cnt)
            cnt=0
print(answer)