def check(n):
    primes=[]
    a = [False,False] + [True]*(n-1)
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes


n = int(input())
lst = check(n)
cnt=0
start = 0
end = 1

while True:
    if end == n:
        break

    val = sum(lst[start:end])

    if val < n:
        end+=1

    elif val > n:
        start+=1

    elif val == n:
        cnt+=1
        start+=1

print(cnt)


