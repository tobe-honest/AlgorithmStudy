global a,b,c

def check(x,y,size):
    temp = board[x][y]
    for i in range(x,x+size,1):
        for j in range(y,y+size,1):
            if temp != board[i][j]:
                return False
    return True 

def divide(x,y,size):
    global a,b,c

    if size==1:
        if board[x][y] == -1:
            a+=1
        elif board[x][y]== 0:
            b+=1
        elif board[x][y]== 1:
            c+=1
        return
    
    if check(x,y,size):
        if board[x][y] == -1:
            a+=1
        elif board[x][y] == 0:
            b+=1
        elif board[x][y] == 1:
            c+=1
        return

    size = size // 3

    divide(x,y,size)
    divide(x,y+size,size)
    divide(x,y+size*2,size)

    divide(x+size,y,size)
    divide(x+size,y+size,size)
    divide(x+size,y+size*2,size)

    divide(x+size*2,y,size)
    divide(x+size*2,y+size,size)
    divide(x+size*2,y+size*2,size)


N = int(input())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
a,b,c=0,0,0
divide(0,0,N)
print(a)
print(b)
print(c)