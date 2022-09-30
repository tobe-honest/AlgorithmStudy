import sys
input=sys.stdin.readline

def recur(a, b, c):
    ## b가 1이면 a%c 반환
    if b == 1:
        return a % c
    ## b가 1이 아니면 b//2로 재귀 호출
    r = recur(a, b//2, c)
    ## b가 짝수면 a^b//2 * a^b//2 => a^b
    ## b가 홀수면 a^b//2 * a^b//2 => a^(b-1)
    ## 그렇기에 a^b//2 * a^b//2 * a^1
    ## 모든 계산값은 c로 나눈 나머지 처리해줌 그래야 시간 빠름
    if not b % 2:
        return r*r%c
    else: return r*r*a%c

a, b, c = map(int, input().split())
print(recur(a, b, c))