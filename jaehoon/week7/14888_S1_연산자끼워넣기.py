import sys
from itertools import permutations

N = int(input())
nums = list(map(int,sys.stdin.readline().split()))
oper = list(map(int,sys.stdin.readline().split()))

oper_str = []
for i in range(4):
    while oper[i] > 0:
        if i == 0:
            oper_str.append("+")
        elif i==1:
            oper_str.append("-")
        elif i==2:
            oper_str.append("*")
        elif i==3:
            oper_str.append("/")
        oper[i]-=1

pos = list(set(permutations(oper_str,N-1)))

answer = []

for i in range(len(pos)):
    result = nums[0]
    for j in range(N-1):
        if pos[i][j] == "+":
            result = result + nums[j+1]
        elif pos[i][j] == "-":
            result = result - nums[j+1]
        elif pos[i][j] == "*":
            result = result * nums[j+1]
        elif pos[i][j] == "/":
            if result < 0 and nums[j+1]>0:
                result = -(-result // nums[j+1])
            else:
                result = result // nums[j+1]
    if i == 0:
        max = result
        min = result

    if max < result:
        max = result
    
    if min > result:
        min = result
    
print(max)
print(min)