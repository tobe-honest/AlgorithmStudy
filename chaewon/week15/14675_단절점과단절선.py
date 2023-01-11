from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
t=defaultdict(list)
for i in range(n-1):
    a,b=map(int,input().split(' '))
    t[a].append(b)
    t[b].append(a)
    
leaf=list()
for i in t.keys():
    if len(t[i])==1:
        leaf.append(i)
        
q=int(input())
for i in range(q):
    dot_or_line, num= map(int,input().split(' '))
    
    if dot_or_line==1:
        #dot
        if n==2 or num in leaf:
            print('no')
        else:
            print('yes')
    else:
        #line
        print('yes')