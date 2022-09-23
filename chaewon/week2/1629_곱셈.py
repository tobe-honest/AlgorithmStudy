import sys
a,b,c= map(int, sys.stdin.readline().split(' '))

def divide(a,b):
    # 종료
    if b==1:
        return a%c
    elif b==2:
        return a*a%c

    # 재귀
    if b%2: # 홀수
        x=divide(a,b//2)
        return x*x*divide(a,1)%c # 나머지들의 제곱과 홀수이기 떄문에 divide(a,1)의 나머지까지 곱해준 후에 c로 나머지
    else : # 짝수
        x=divide(a,b//2)
        return x*x%c # 나머지들의 곱과 c로 나머지
print(divide(a,b))
