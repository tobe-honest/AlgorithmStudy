def moo(k,start,end,wing,body):

    target = start + wing
    if target == N:
        print('m')
        return
    elif N < target:
        moo(k-1,start,target-1,(wing-body+1)//2,body-1)
    elif N >= target+body:
        moo(k-1,target+body,end,(wing-body+1)//2,body-1)
    else:
        print('o')
        return
    

N = int(input())
wing,body,k = 3,4,1

while True:
    if wing*2+body >= N:
        break
    wing = wing*2+body
    body += 1
    k += 1

moo(k,1,wing*2+body,wing,body)
