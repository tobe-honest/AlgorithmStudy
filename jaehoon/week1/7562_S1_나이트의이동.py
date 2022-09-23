from collections import deque

dx = [-1,1,-2,2,-2,2,-1,1]
dy = [-2,-2,-1,-1,1,1,2,2]

def move(x,y,visited,level):
    visited[y][x] = True
    queue = deque([[y,x]])
    level[y][x] = 0

    while queue:
        Y,X = queue.popleft()

        for i in range(8):
            kx , ky = X + dx[i] , Y + dy[i]

            if kx < 0 or kx >= size or ky < 0 or ky >= size or visited[ky][kx] == True:
                continue

            visited[ky][kx] = True
            queue.append([ky,kx])
            level[ky][kx] = level[Y][X] + 1


iteration = int(input())
for i in range(iteration):
    size = int(input())
    x,y = map(int,input().split())
    target_x,target_y = map(int,input().split())

    visited = [[False for i in range(size)] for j in range(size)]
    visited = [False for i in range(size) for j in range(size) for k in range(size)]
    print(visited,len(visited))
    break
    level = [[0 for i in range(size)] for j in range(size)]

    move(x,y,visited,level)
    print(level[target_y][target_x])
    
    