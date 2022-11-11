t=int(input())
for _ in range(t):
    score=[] #[(선수,포지션,점수)]

    for i in range(11): # 선수
        tmp=list(map(int,input().split(' ')))
        for j in range(11): #포지션
            if tmp[j]!=0:
                score.append((i,j,tmp[j]))
        
    print(score)
