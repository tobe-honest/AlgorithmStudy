from collections import deque

global count

def check(x,y):

    global count

    if x < 0 or x >= N or y < 0 or y >= N or board[x][y] == 0 or visited[x][y] == True:
        return

    if visited[x][y] == False:
        visited[x][y] = True
        count+=1
        check(x-1,y)
        check(x+1,y)
        check(x,y-1)
        check(x,y+1)


N = int(input())
board,arr,num,count = [], [], 0, 0

for i in range(N): board.append(list(map(int,input())))
visited = [[False for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == False:
            check(i,j)
            arr.append(count)
            num, count = num+1, 0
            
print(num)
arr.sort()
for i in range(num): print(arr[i])

