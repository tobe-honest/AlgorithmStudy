import sys

N = int(input())
lst,result = [],[]
for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in range(N):
    result.append(lst[i]*(N-i))

print(max(result))