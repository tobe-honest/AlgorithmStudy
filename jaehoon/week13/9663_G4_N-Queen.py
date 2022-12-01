from collections import deque

def solution(depth):
    global result
    
    if depth == n:
        result+=1
        return

    for i in range(n):
        # if visit[i] == 1:
        #     continue

        queen[depth] = i
        flag = 0

        for j in range(depth):
            if queen[depth] == queen[j] or abs(depth-j) == abs(queen[depth] - queen[j]):
                flag = 1
                break

        if flag == 0:
            #visit[i] = 1
            solution(depth+1)
            #visit[i] = 0

if __name__ == "__main__":
    n = int(input())
    result = 0
    queen = [0] * n
    visit = [0] * n
    solution(0)
    print(result)


