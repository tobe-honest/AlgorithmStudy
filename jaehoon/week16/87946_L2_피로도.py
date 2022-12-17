answer, N = 0,0

def function(k, depth, dungeons,visit):
    global answer
    answer = max(answer,depth)

    for i in range(N):
        if k >= dungeons[i][0] and visit[i] == False:
            visit[i] = True
            function(k - dungeons[i][1], depth + 1, dungeons,visit)
            visit[i] = False

def solution(k, dungeons):
    global N, visit
    N = len(dungeons)
    visit = [0] * N
    function(k, 0, dungeons,visit)
    return answer