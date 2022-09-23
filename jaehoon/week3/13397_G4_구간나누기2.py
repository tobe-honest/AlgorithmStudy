N,M = map(int,input().strip().split())
lst = list(map(int,input().strip().split()))

def divide(x):
  max_x=min_x=lst[0]
  cnt=1
  for i in range(1,N):
    max_x=max(max_x,lst[i])
    min_x=min(min_x,lst[i])
    if max_x - min_x > x:
      cnt+=1
      max_x=lst[i]
      min_x=lst[i]
  return cnt

start, end = 0, max(lst)
result=0
while start<=end:
  mid=(start+end)//2
  if divide(mid) <= M:
    end = mid-1
    result=mid
  else:
    start = mid+1

print(result)