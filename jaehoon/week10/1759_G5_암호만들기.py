from itertools import combinations
L,C = map(int,input().split())
lst = list(input().split())

result = []
candidate = list(combinations(lst,L))
for i in range(len(candidate)):
    temp = sorted(candidate[i])
    result.append(temp)

result.sort()
answer=[]
for i in range(len(result)):
    vow,con = 0,0 #모음, 자음 개수
    for word in result[i]:
        if word in 'aeiou':
            vow+=1
        else:
            con+=1
    if vow>=1 and con>=2:
        answer.append(result[i])


for i in range(len(answer)):
    print("".join(answer[i]))