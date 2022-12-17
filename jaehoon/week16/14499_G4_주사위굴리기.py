import sys

n,m,x,y,k = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
orders = list(map(int,sys.stdin.readline().split()))
dice = [0,0,0,0,0,0] # 바닥 남쪽 천장 북쪽 서쪽 동쪽

for order in orders:
    flag=0
    temp = dice[:]

    if order == 1:
        x,y = x,y+1
        if x<0 or y<0 or x>=n or y>=m:
            x,y = x,y-1
            continue
        
        dice[5] = temp[0]
        dice[1] = temp[1] 
        dice[4] = temp[2]
        dice[3] = temp[3]
        dice[0] = temp[4]
        dice[2] = temp[5]
        flag=1
        
    elif order == 2:
        x,y = x,y-1
        if x<0 or y<0 or x>=n or y>=m:
            x,y = x,y+1
            continue

        dice[4] = temp[0]
        dice[1] = temp[1] 
        dice[5] = temp[2]
        dice[3] = temp[3]
        dice[2] = temp[4]
        dice[0] = temp[5]
        flag=1

    elif order == 3:
        x,y = x-1,y
        if x<0 or y<0 or x>=n or y>=m:
            x,y = x+1,y
            continue

        dice[1] = temp[0]
        dice[2] = temp[1] 
        dice[3] = temp[2]
        dice[0] = temp[3]
        dice[4] = temp[4]
        dice[5] = temp[5]
        flag=1

    elif order == 4:
        x,y = x+1,y
        if x<0 or y<0 or x>=n or y>=m:
            x,y=x-1,y
            continue

        dice[3] = temp[0]
        dice[0] = temp[1] 
        dice[1] = temp[2]
        dice[2] = temp[3]
        dice[4] = temp[4]
        dice[5] = temp[5]
        flag=1
    
    if board[x][y] == 0:
            board[x][y] = dice[0]
    else:
        dice[0] = board[x][y]
        board[x][y] = 0
    
    if flag==1:
        print(dice[2])