g=int(input())
now, remember, flag, dif =2,1,True,0
while now<100000:
    dif=now**2-remember**2
    
    if dif>g:
        if now-remember==1:
            break
        remember+=1
    elif dif<g:
        now+=1
    elif dif==g:
        print(now)
        flag=False
        now+=1
        remember+=1
if flag:
    print(-1)