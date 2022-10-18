def check(lst):
    visit = [False] * N

    for i in range(N-1):
        if lst[i] == lst[i+1]:
            continue

        if abs(lst[i] - lst[i+1]) > 1:
            return False

        elif abs(lst[i] - lst[i+1]) == 1:
            if lst[i] - lst[i+1] > 0:  # 내리막길
                if i+1+L <= N:
                    std = lst[i+1]
                    for j in range(i+1,i+1+L):
                        if lst[j] != std or visit[j] == True:
                            return False
                    visit[i+1:i+1+L] = [True] * L
                else:
                    return False


            else: # 오르막길
                if 0<= i-L+1:
                    std = lst[i]
                    for j in range(i-L+1,i+1):
                        if lst[j] != std or visit[j] == True:
                            return False
                    visit[i-L+1:i] = [True] * L
                else:
                    return False
    
    return True


N, L = map(int,input().split())
board,cnt = [],0
for i in range(N):
    board.append(list(map(int,input().split())))

# 내 위치가 x일 때, 경사 올라갈 떄는 x-1, x-2...체크 / 경사 내려갈 때는 x+1,x+2...체크

for i in range(N): # 행 검사
    lst = board[i][:]
    if check(lst):
        cnt+=1

for i in range(N): #열 검사
    lst = list(zip(*board))[i]
    if check(lst):
        cnt+=1
print(cnt)

