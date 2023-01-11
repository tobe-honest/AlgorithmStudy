import sys 
from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate(line,k,d):
    if d== 0:
        for _ in range(k):
            line.appendleft(line.pop())
    else : 
        for _ in range(k):
            line.append(line.popleft())

def check(board,n,m):
    temp_board = [deque([board[i][j] for j in range(m)]) for i in range(n)]
    check = False 

    for i in range(n):
        for j in range(m): 
            for k in range(4):
                nx,ny = i+dx[k], (j+dy[k])%m
                if 0<=nx<n and 0<=ny<m and board[i][j] != 0 and board[i][j] == board[nx][ny] : 
                    temp_board[nx][ny] = 0
                    temp_board[i][j] = 0
                    check = True

    if not check: 
        cum,cnt = 0,0

        for i in range(n):
            for j in range(m):
                cum += board[i][j]
                if board[i][j] : 
                    cnt+=1

        if cnt == 0 : 
            return board, False 

        avg = cum/cnt
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 : 
                    continue 
                if board[i][j] < avg :
                    temp_board[i][j] += 1 
                elif board[i][j] > avg :
                    temp_board[i][j] -= 1

    return temp_board,True 

if __name__ == "__main__":
    n,m,t = map(int,sys.stdin.readline().split())
    board = []
    for i in range(n):
        board.append(deque(list(map(int,sys.stdin.readline().split()))))

    for _ in range(t) :  
        x,d,k = map(int,input().split())
        for i in range(x,n+1,x):
            rotate(board[i-1],k,d)
        board,check_board = check(board,n,m)
        if not check_board :
            break
    
    result =0 
    for line in board:
        result += sum(line)
    print(result)