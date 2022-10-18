import sys

def check2(air, board):

    #up
    a = air[0]
    prev = 0
    for i in range(1,C):
        next = board[a][i]
        board[a][i] = prev
        prev = next

    for i in range(1,a):
        next = board[a-i][C-1]
        board[a-i][C-1] = prev
        prev = next

    for i in range(1,C+1):
        next = board[0][C-i]
        board[0][C-i] = prev
        prev = next

    for i in range(1,a):
        next = board[i][0]
        board[i][0] = prev
        prev = next

    #down
    prev = 0
    b=air[1]
    for i in range(1,C):
        next = board[b][i]
        board[b][i] = prev
        prev = next

    for i in range(1,R-b):
        next = board[b+i][C-1]
        board[b+i][C-1] = prev
        prev = next
    
    for i in range(1,C):
        next = board[R-1][C-1-i]
        board[R-1][C-1-i] = prev
        prev = next

    for i in range(1,R-b):
        next = board[R-1-i][0]
        board[R-1-i][0] = prev
        prev = next

    board[air[0]][1] = 0
    board[air[1]][1] = 0
    board[air[0]][0] = -1
    board[air[1]][0] = -1
    return board

def check1(board):
    origin = [[0 for col in range(C)] for row in range(R)]
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for i in range(R):
        for j in range(C):
            cnt = 0
            if board[i][j] !=0 and board[i][j] != -1:
                for di,dj in d:
                    ky,kx = i+di, j+dj

                    if ky<0 or kx<0 or ky>=R or kx>=C or board[ky][kx]==-1:
                        continue

                    origin[ky][kx] =  origin[ky][kx] + board[i][j]//5
                    cnt += 1

            board[i][j] = board[i][j] - board[i][j]//5*cnt

    for i in range(R):
        for j in range(C):
            board[i][j] += origin[i][j]
    
    return board


if __name__ == '__main__':
    R,C,T = map(int,input().split())
    board = []
    for _ in range(R):
        board.append(list(map(int,sys.stdin.readline().split())))

    air = []
    for i in range(R):
        if board[i][0] == -1:
            air.append(i)
            air.append(i+1)
            break

    for _ in range(T):
        board=check1(board)
        board=check2(air,board)

    result = 0
    for i in range(R):
        for j in range(C):
            result += board[i][j]

    print(result+2)