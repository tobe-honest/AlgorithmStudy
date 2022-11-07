from itertools import combinations
def solution(orders, course):
    answer = []
    for r in course:
        tmp=set()
        for order in orders:
            order=set(order)
            order=list(order)
            order.sort()
            tmp.update(list(combinations(order,r)))
        count=dict()
        for t in tmp:
            count[''.join(t)]=0
        # 몇번 있었나 세기
        for case in count.keys():
            for order in orders: 
                flag=True
                for c in case:
                    if c in order:
                        continue
                    else:
                        flag=False
                        break
                if flag:
                    count[case]+=1
        candidate=list(count.values())
        if len(candidate)>0:
            max_value=max(count.values())
            if max_value>=2:
                for case in count.keys():
                    if count[case]==max_value:
                        answer.append(case)
    answer.sort()
    return answer