# 일관서 유지 조건 : 한 번호가 다른 번호의 접두어인 경우가 없어야 함

import sys
input = sys.stdin.readline

for _ in range(int(input())): # t
    number = [input().rstrip() for _ in range(int(input()))]
    number.sort()
    flag = False
    for i in range(len(number)-1):
        if number[i+1].startswith(number[i]):
            flag = True
            break
    # print(number)
    print("NO") if flag else print("YES")