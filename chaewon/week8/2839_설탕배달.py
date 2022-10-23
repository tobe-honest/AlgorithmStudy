import sys
input=sys.stdin.readline
kg=int(input())
answer=0
answer+=kg//5
rest=kg%5
flag=False
kg=kg-rest
if rest==0:
    print(answer)
    exit()
else:
    while kg>=0:
        
        if rest%3!=0:
            answer-=1
            rest+=5
            kg-=5
        else:
            answer+=rest//3
            flag=True
            break
if flag:
    print(answer)
else:
    print(-1)