from itertools import combinations
def solution(number):
    answer = 0
    candidate = list(combinations(number,3))
    
    for lst in candidate:
        if sum(lst) == 0:
            answer+=1
            
    return answer