# 일관서 유지 조건 : 한 번호가 다른 번호의 접두어인 경우가 없어야 함

# for _ in range(int(input())): # t
#     n = int(input())
#     number_list = [i for i in range(10)]
#     flag = False

#     sorted_number = sorted([input() for _ in range(n)], reverse=True)

#     for number in sorted_number:
#         j = 0
#         cnt = 0
#         while j < len(number):
#             if int(number[j]) in number_list

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