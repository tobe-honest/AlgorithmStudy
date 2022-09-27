import sys

N = int(input())
lst_start, lst_end, cnt = [], [], 0

for i in range(N):
    id,start,end = map(int,sys.stdin.readline().split())
    lst_start.append(start)
    lst_end.append(end)

lst_start.sort()
lst_end.sort()

for i in range(N):
    if lst_end[0]>lst_start[i]:
        cnt+=1
    else:
        del lst_end[0]

print(cnt)

