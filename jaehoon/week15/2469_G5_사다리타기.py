import sys

n = int(input())
m = int(input())
finish = list(map(str, sys.stdin.readline().strip()))
start = sorted(finish)
board1,board2 = [], []
flag = 0

for i in range(m):
    line = list(map(str,input().strip()))
    
    if line[0] == '?':
        flag=1
    
    if flag==0:
        board1.append(line)
    else:
        board2.append(line)
    
while board1:
    line = board1.pop(0)
    for i in range(n-1):
        if line[i] == '-':
            start[i], start[i+1] = start[i+1], start[i] 

while board2:
    line = board2.pop()
    for i in range(n-1):
        if line[i] == '-':
            finish[i], finish[i+1] = finish[i+1], finish[i]

result = ['*' for _ in range(n-1)]

for i in range(n-1):
    if start[i] == finish[i+1] and start[i+1] == finish[i]:
        result[i] = '-'
        start[i], start[i+1] = start[i+1], start[i]

if start != finish:
    result = ['x' for _ in range(n-1)]
print(''.join(result))