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

#  readline에서는 rstrip이 필요
# dfs에서 무리 별 번호는 따로 카운트 가능
# dictionary에서 lambda 표현식 사용법 이해
# list comprehension으로 쉽게 입력 가능
# dictionary.get으로 key가 있는지 확인 가능
# 전역 변수는 함수 내부에서 global로 접근 가능