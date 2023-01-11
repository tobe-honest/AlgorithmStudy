answer = 0
def permutation(arr,visited,r,dungeons,k):
    global answer
        
    for i in range(r):
        if not visited[i]:
            arr.append(i)
            visited[i]=True
            
            is_possible, cnt = count_dungeons(arr,dungeons,k)
            if is_possible:
                answer=max(answer,cnt)
                permutation(arr[:],visited[:],r,dungeons,k)
            arr.pop()
            visited[i]=False
def count_dungeons(per, dungeons,k):
    cnt=0
    for p in per:
        if k>=dungeons[p][0]:
            k-=dungeons[p][1]
            cnt+=1
        else:
            return False,cnt
    return True,cnt
def solution(k, dungeons):
    dungeons.sort(reverse=True)
    global answer
    permutation([],[False]*len(dungeons),len(dungeons),dungeons,k)

    return answer