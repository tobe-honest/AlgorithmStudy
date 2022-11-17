def check_square(board):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] == 0:
                continue
            if board[i][j] == 1 and board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1] == 1:
                cnt+=1
    return cnt

def make_dragon(board,x,y,d,g):
    lst = [d]
    for i in range(g):
        leng = len(lst)
        for j in range(leng):
            val = (lst[leng-j-1]+1) % 4
            lst.append(val)
    
    board[y][x] = 1
    for val in lst:
        if val == 0:
            x+=1
            board[y][x] = 1
        
        elif val == 1:
            y-=1
            board[y][x] = 1
        
        elif val == 2:
            x -= 1
            board[y][x] = 1

        elif val == 3:
            y += 1
            board[y][x] = 1

    return board

n = int(input())
board = [[0 for j in range(101)] for i in range(101)]
for i in range(n):
    x,y,d,g = map(int,input().split())
    board = make_dragon(board,x,y,d,g)

print(check_square(board))