permus=list()
def permutation(arr,visited,r):
    if len(arr)==r:
        permus.append(arr)
        
    for i in range(r):
        if not visited[i]:
            arr.append(i)
            visited[i]=True
            permutation(arr[:],visited[:],r)
            arr.pop()
            visited[i]=False
def count_dungeons(per, dungeons,k):
    cnt=0
    
    for p in per:
        if k>=dungeons[p][0]:
            k-=dungeons[p][1]
            cnt+=1
        else:
            return cnt
    return cnt
def solution(k, dungeons):
    dungeons.sort(reverse=True)
    answer = 0
    permutation([],[False]*len(dungeons),len(dungeons))
    
    for per in permus:
        answer=max(answer,count_dungeons(per,dungeons,k))
    return answer