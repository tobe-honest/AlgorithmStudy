from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for size in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), size)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    
    return sorted(answer)