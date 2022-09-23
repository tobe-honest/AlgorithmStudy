import sys
sys.setrecursionlimit(5000)

def check(x,y,type,visited):
    if x < 0 or x >= N or y < 0 or y >=N or visited[x][y]==True:
        return
    
    if board[x][y]==type:
        visited[x][y] = True
        if board[x][y] == 'G':
            board[x][y] = 'R'
        check(x-1,y,type,visited)
        check(x+1,y,type,visited)
        check(x,y-1,type,visited)
        check(x,y+1,type,visited)


N = int(input())
board = []
for i in range(N):
    line = list(sys.stdin.readline().rstrip())
    board.append(line)
    
count_A,count_B = 0, 0
visited_A = [[False for i in range(N)] for j in range(N)]
visited_B = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if visited_A[i][j] == False:
            check(i,j,board[i][j],visited_A)
            count_A+=1

for i in range(N):
    for j in range(N):
        if visited_B[i][j] == False:
            check(i,j,board[i][j],visited_B)
            count_B+=1
print(count_A,count_B)