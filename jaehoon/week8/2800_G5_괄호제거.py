import sys
from itertools import combinations

string = list(map(str, sys.stdin.readline().strip()))
stack, pos, result = [], [], set()

for i in range(len(string)):
    if string[i] == '(':
        stack.append(i)
    if string[i] == ')':
        pos.append((stack.pop(), i))

for i in range(1,len(pos)+1):
    cases = list(combinations(pos,i))
    for case in cases:
        temp = string[:]
        for a,b in case:
            temp[a] = ''
            temp[b] = ''
        result.add(''.join(temp))

for i in sorted(list(result)):
    print(i)