import sys
input = sys.stdin.readline

# def Moo(n, length_l):
#     if n == 0:
#         length_l[n+1] = 3
#         return 3
#     length = Moo(n-1, length_l)
#     length_l[n+1] = length*2 + n + 3
#     return length_l[n+1]

def Moo(n):
    if n == 1:
        return "m"
    if n == 2 or n == 3:
        return "o"
    idx = 0
    while length_l[idx] < n: idx += 1

    ## n이 S(n-1) + 1 위치를 가르킨다면 m
    if length_l[idx-1] + 1 == n: return "m"
    ## n이 S(n)의 길이와 같다면(o라면)
    ## n이 S(n-1)의 길이 + S(n)의 중간 부분의 길이보다 작거나 같다면 o (3분할에서 중간 부분이라면)
    if length_l[idx] == n or length_l[idx-1] + idx + 3 >= n: return "o"
    ## n이 S(n-1)의 길이 + S(n)의 중간 부분의 길이보다 길다면(3분할에서 마지막 부분이라면)
    ## S(n-1)에서 판별
    ## length_l[idx-1]로 리턴하면 안됨
    ## ==> n-length_l[idx-1]-(idx+3) 1, 2, 3인 부분 케어가 안됨
    return Moo(n-length_l[idx-1]-(idx+3))

N = int(input())
length_l = [0 for i in range(29)]
length_l[0] = 3
for i in range(1, 29):
    length_l[i] = 2*length_l[i-1] + i+3
print( Moo(N) )

    
# S(1)에서의 m은 
# [S(0)에서의 m위치, S(0)의 길이 + 1의 위치, S(0)의 길이 + n+4의 위치]
# 3분할 갈라서 구하기.
