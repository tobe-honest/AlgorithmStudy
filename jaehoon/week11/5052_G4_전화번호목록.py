import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(input())
    numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
    numbers.sort()
    flag=1

    for i in range(N-1):
        temp = len(numbers[i])
        if numbers[i] == numbers[i+1][:temp]:
            flag=0
            break
    
    if flag:
        print("YES")
    else:
        print("NO")