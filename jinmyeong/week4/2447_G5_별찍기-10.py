import copy
import sys
input = sys.stdin.readline


N = int(input())
m = N // 3
result = [["***"], ["* *"], ["***"]]

while len(result[0][0]) != N:
    for i in range(len(result)):
        result[i][0] *= 3
    tmp = copy.deepcopy(result)
    for i in range(2):
        for t in tmp:
            result.append(copy.deepcopy(t))

    length = len(result[0][0])//3
    for i in range(length, length*2):
        result[i][0] = result[i][0][:length] + " " * length + result[i][0][2*length:]
    
print('\n'.join(i[0] for i in result))


    