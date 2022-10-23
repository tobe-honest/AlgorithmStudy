import sys
from itertools import combinations
form=sys.stdin.readline()
list_form=list() # 각 문자열을 하나하나 떼서 넣은 리스트
start, pair =list(),list() # start : (가 시작되는 인덱스 저장 # pair : 괄호 쌍을 저장
for i,f in enumerate(form):
    list_form.append(f)
    if f=='(':
        start.append(i)
    elif f==')':
        pair.append([start.pop(), i])

answer=set()
for r in range(1,len(pair)+1):
    cases=list(combinations(range(len(pair)),r)) # nCr
    for case in cases: 
        form_cp=list_form[:]
        del_list=list()
        for c in case:
            del_list+=pair[c] # 제거해야할 인덱스들을 del_list에 넣음
        del_list.sort(reverse=True) # 제거할 때 거꾸로 해야 에러 안 뜸
        for i in range(0,len(del_list)):
            del form_cp[del_list[i]] # 괄호 제거
        answer.add(''.join(form_cp)) # 만들어진 하나의 문자열

answer=list(answer)
answer.sort()
for a in answer:
    print(a) 