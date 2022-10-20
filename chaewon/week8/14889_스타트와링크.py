import sys
from itertools import combinations
input=sys.stdin.readline

n=int(input())
s=list()
for i in range(n):
    s.append(list(map(int, input().split(' '))))

def make_sum(can):
    result=0
    for i in can:
        for j in can:
            result+= s[i][j]
    return result

candidates=list(combinations(range(n),n//2))
answer=int(1e9)
for can in candidates:
    x=list()
    for i in range(n):
        if i not in can:
            x.append(i)
        if len(x)==n//2:
            flag=True
            break

    sum_can=make_sum(can)
    sum_x=make_sum(x)
    answer=min(abs(sum_can-sum_x), answer)

print(answer)