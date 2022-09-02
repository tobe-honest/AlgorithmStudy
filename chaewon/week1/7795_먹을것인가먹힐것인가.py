case=int(input())
for _ in range(case):
    n,m=map(int,input().split(' '))
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    cnt=0
    a.sort(reverse=True)
    b.sort(reverse=True)

    a_now,b_now=0,0

    while a_now<n and b_now<m:
        if a[a_now]>b[b_now]:
            cnt=cnt+ m -b_now
            a_now+=1
        else:
            b_now+=1
    print(cnt)
