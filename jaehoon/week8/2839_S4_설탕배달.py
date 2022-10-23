N = int(input())
cnt = 0

while N%5!=0:
    if N<0:
        print(-1)
        exit()
    N,cnt = N-3,cnt+1

print(cnt + N//5)