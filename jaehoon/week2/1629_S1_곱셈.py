def cal(a,b):
    temp = cal(a,b//2)%c
    if b%2==0:
        return temp*temp
    if b%2!=0:
        return temp*temp*a

a,b,c = list(map(int,input().split()))
print(6%8)
##print(cal(a,b)%c)

