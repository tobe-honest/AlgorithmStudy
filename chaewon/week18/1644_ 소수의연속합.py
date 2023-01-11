n=int(input())

def make_primenum(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

if n==1:
    print(0)        
else:
    primes=make_primenum(n)
    answer=0
    s,e=0,1
    sum_now=primes[0]
    len_primes=len(primes)
    while s<len_primes:
        if e>len_primes:
            e=len_primes
        if sum_now==n:
            answer+=1
            sum_now-=primes[s]
            s+=1
            e+=1
            if e<=len_primes:
                sum_now+=primes[e-1]
        elif sum_now<n:
            if e < len_primes:
                e+=1
                sum_now+=primes[e-1]
            else:
                break
        else: # sum_now > n
            if e-s==1:
                break
            else:
                sum_now-=primes[s]
                s+=1
    print(answer)