from collections import Counter
import sys
input = sys.stdin.readline

def dfs(x, y):
    global arr
    global dic
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if arr[x][y] == 1:
        arr[x][y] = k

        dfs(x-1, y)        
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        if dic.get(k) is None:
            dic[k] = 1
        else:
            dic[k] += 1

        return True
    return False

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0
k = 2
dic = {}

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
            k+=1

print(cnt)

for dic in sorted(dic.items(), key = lambda x : x[1]):
    print(dic[1])