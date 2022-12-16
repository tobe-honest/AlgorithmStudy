import sys
input=sys.stdin.readline
n,s=map(int, input().split(' '))
seq=list(map(int, input().split(' ')))
answer=0

def ncr(now,start):
    global answer
    if sum(now)==s and len(now)>0:
        answer+=1

    if len(now)==n:
        return
    
    for i in range(start,n):
        now.append(seq[i])
        ncr(now[:],i+1)
        now.pop()

ncr([],0)
print(answer)