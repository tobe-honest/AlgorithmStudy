
def star(k,x,y):
    if k==0:
        return

    for i in range(k):
        for j in range(k):
            board[x+i][y+j] = " "

    k = k//3
    star(k,x-2*k,y-2*k)
    star(k,x+k,y-2*k)
    star(k,x+4*k,y-2*k)

    star(k,x-2*k,y+k)
    star(k,x+k,y+k)
    star(k,x+4*k,y+k)

    star(k,x-2*k,y+4*k)
    star(k,x+k,y+4*k)
    star(k,x+4*k,y+4*k)

N = int(input())

board = []
for i in range(N):
    line = ["*"] * N
    board.append(line)
    line = []

N = N//3
star(N,N,N)
for i in range(N*3):
    print(''.join(board[i]))
    