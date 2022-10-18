
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def cal(y,x,info):
    target = board[y][x]
    cnt=0
    for k in range(4):
        ky,kx = y+dy[k], x+dx[k]
        if ky<0 or kx<0 or ky>=N or kx>=N:
                continue

        if board[ky][kx] == info[target-1][1] or board[ky][kx] == info[target-1][2] or board[ky][kx] == info[target-1][3] or board[ky][kx] == info[target-1][4]:
            cnt+=1

    if cnt==0:
        return 0
    elif cnt==1:
        return 1
    elif cnt==2:
        return 10
    elif cnt==3:
        return 100
    elif cnt==4:
        return 1000

def condition2(info,target):

    candidate=[]
    for i in range(len(info)):
        cnt=0
        if board[info[i][1]][info[i][2]] != 0:
            continue

        for k in range(4):
            ky,kx = info[i][1]+dy[k], info[i][2]+dx[k]

            if ky<0 or kx<0 or ky>=N or kx>=N:
                    continue

            if board[ky][kx] == 0:
                cnt+=1
        
        candidate.append([cnt,info[i][1],info[i][2]])
    candidate = sorted(candidate, key=lambda x : -x[0])
    board[candidate[0][1]][candidate[0][2]] = target


def condition1(info):

    candidate=[]

    for y in range(N):
        for x in range(N):
            cnt = 0
            if board[y][x] != 0:
                continue
            for k in range(4):
                ky,kx = y + dy[k], x + dx[k]
                
                if ky<0 or kx<0 or ky>=N or kx>=N:
                    continue

                if board[ky][kx] == info[1] or board[ky][kx] == info[2] or board[ky][kx] == info[3] or board[ky][kx] == info[4]:
                    cnt+=1
            
            candidate.append([cnt,y,x])

    candidate = sorted(candidate, key=lambda x : -x[0])
    min = candidate[0][0]
    l=[]
    for i in range(len(candidate)):
        if min<=candidate[i][0]:
            l.append(candidate[i])       

    if len(l)==1:
        board[l[0][1]][l[0][2]] = info[0]
    else:
        condition2(l,info[0])
    


N = int(input())

board,lst = [[0 for x in range(N)]for k in range(N)],[]
for i in range(N**2):
    lst.append(list(map(int,input().split())))

for i in range(len(lst)):
    condition1(lst[i])


result = 0
lst = sorted(lst, key=lambda x : x[0])

for i in range(N):
    for j in range(N):
        result += cal(i,j,lst)

print(result)