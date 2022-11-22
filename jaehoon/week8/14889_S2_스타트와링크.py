import sys
from itertools import combinations
N = int(input())
board,min = [], int(1e9)
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
items = [i for i in range(1,N+1)]
lst = list(combinations(items,N//2))
cases = [value for value in lst if value[0] == 1]
for case in cases:
    start,link = 0,0
    B = set(items) -set(case)

    for i in range(N):
        if i+1 in case:
            for j in case:
                start+=board[i][j-1]

        else:
            for j in B:
                link+=board[i][j-1]
    
    gap = abs(start-link)
    if gap < min:
        min = gap

print(min)