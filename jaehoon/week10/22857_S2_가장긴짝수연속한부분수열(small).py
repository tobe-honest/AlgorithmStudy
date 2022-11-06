import sys

N,K = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
start,end,cnt,result = 0,-1,0,0

while True :
    if cnt <= K :
        result = max(result, end-start+1 - cnt)

    if cnt <= K :
        end += 1
        if end >= N :
            break

        if lst[end] % 2 == 1 :
            cnt +=1
        
    else :
        if lst[start] % 2 == 1 :
            cnt -=1

        start+=1
        if start > end :
            break
        
print(result)