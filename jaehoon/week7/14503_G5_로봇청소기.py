def check_left(y,x,d):
    if d==0:
        y,x = y,x-1
    elif d==1:
        y,x = y-1,x
    elif d==2:
        y,x = y,x+1
    elif d==3:
        y,x = y+1,x
    
    if 0<=x<M and 0<=y<N and board[y][x] == 0 and visit[y][x] == False:
        return True
    else:
        return False

def turn(d):
    if d==0:
        return 3
    else:
        return d-1


def move(y,x,d):
    if d == 0:
        y,x = y-1,x
    elif d==1:
        y,x = y,x+1
    elif d==2:
        y,x = y+1,x
    elif d==3:
        y,x = y,x-1

    return y,x 

def back(y,x,d):
    if d == 0:
        y,x = y+1,x
    elif d==1:
        y,x = y,x-1
    elif d==2:
        y,x = y-1,x
    elif d==3:
        y,x = y,x+1

    if 0<=x<M and 0<=y<N and board[y][x] == 0:
        return y,x,True
    else:
        return y,x,False




def check(y,x,d):
    result = 0

    while True:
        visit[y][x] = True
        result+=1
        cnt=0
        while True:
            if check_left(y,x,d):
                d = turn(d)
                y,x = move(y,x,d)
                break
            else:
                d = turn(d)
                cnt+=1

                if cnt==4:
                    y,x,ok = back(y,x,d)
                    cnt=0
                    if ok==False:
                        return result
                continue

            
N, M = map(int,input().split())
y,x,d = map(int,input().split())
board = []
visit = [[False for x in range(M)] for y in range(N)]
for i in range(N):
    board.append(list(map(int,input().split())))

print(check(y,x,d))
