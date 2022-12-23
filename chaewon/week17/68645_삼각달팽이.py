def solution(n):
    answer = [[-1]*n for _ in range(n)]
    end=0
    for i in range(n):
        for j in range(i+1):
            answer[i][j]=0
            end+=1
    idx=1
    length= n-1
    round=0
    now_x=0
    now_y=0
    if n==1:
        return [1]
    else:
        while idx<=end:

            #1111111111111
            for i in range(length):
                answer[now_x+i][now_y]=idx
                idx+=1
            now_x+=length

            if idx>end:
                break

            # 222222222222222
            for i in range(length):
                answer[now_x][now_y+i]=idx
                idx+=1
            now_y+=length
            if idx>end:
                break

            # 3333333333333333333
            for i in range(length):
                answer[now_x-i][now_y-i]=idx
                idx+=1
            now_x=now_x-length+2
            now_y=now_y-length+1

            round+=1
            length-=3
            if length==0:
                length=1

    result=[]
    for i in range(n):
        for j in range(i+1):
            result.append(answer[i][j])
    return result