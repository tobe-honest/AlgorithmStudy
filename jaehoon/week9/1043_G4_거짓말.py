import sys
N, M = map(int,input().split())
know = list(map(int,input().split()))
board = []
if know[0] == 0:
    print(M)
    exit()
else:
    know = set(know[1:])
    for i in range(M):
        lst = list(map(int,input().split()))
        board.append(lst)
        
        for j in range(1,len(lst)):
            if lst[j] in know:
                for k in range(1,len(lst)):
                    know.add(lst[k])
                break

visit = [False for i in range(M)]

for p in range(2):
    for i in range(M):
        if visit[i] == True:
            continue
        temp = board[i][1:]
        for j in range(len(temp)):
            if temp[j] in know:
                for k in range(len(temp)):
                    know.add(temp[k])
                visit[i] = True

cnt = 0
for i in range(M):
    temp = set(board[i][1:])
    if len(temp&know) < 1:
        cnt+=1

print(cnt)
        

        
