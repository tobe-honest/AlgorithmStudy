from itertools import combinations

x=list(map(int, input().split(' ')))

while True:
    answer=list(combinations(x[1:],6))
    for ans in answer:
        tmp=''
        for a in ans:
            tmp+=f'{a} '
        print(tmp)
    x=list(map(int, input().split(' ')))
    if x==[0]:
        break
    print()