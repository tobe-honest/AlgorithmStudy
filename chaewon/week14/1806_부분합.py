n, aim=map(int,input().split(' '))
seq=list(map(int,input().split(' ')))

now_sum=seq[0]
start,end=0,1
min_len=1e9

while start<n:
    if end-start==1: # 길이가 1일 때
        if end<n-1:
            end+=1
            now_sum+=seq[end]
            if now_sum>=aim:
                min_len=min(min_len,end-start)
    if now_sum<aim:
        if end<n-1:
            end+=1
            now_sum+=seq[end]
            if now_sum>=aim:
                min_len=min(min_len,end-start)
        else: # end도 끝까지 왔는데 now_sum도 목표치보다 낮으면 이제 start만 커지는데 그럼 더 작아지는 일 밖에 안 남음
            break
    else: # 목표치보다 값이 큼
        start+=1
        now_sum-=seq[start]
print(min_len)