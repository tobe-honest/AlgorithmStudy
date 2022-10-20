import sys
input=sys.stdin.readline
n,m=map(int, input().split())
robot_x, robot_y, direction=map(int, input().split())
graph=list()
for _ in range(n):
    graph.append(list(map(int, input().split())))

left={0:3,3:2,2:1,1:0}
def search_next(x, y, direction):
    
    for i in range(4):
        # 현재 방향에서 왼쪽 좌표 반환 -> next_x, next_y # turn left
        if direction==0:
            next_x, next_y=x, y-1
        elif direction==1:
            next_x, next_y=x-1, y
        elif direction==2:
            next_x, next_y=x, y+1
        elif direction==3:
            next_x, next_y=x+1, y
        direction = left[direction]
        if 0< next_x<n-1 and 0< next_y<m-1: # 양 끝 벽 뺌
            if graph[next_x][next_y]==0: # 청소할 다음 위치
                return next_x, next_y, direction

    # 뒤로
    if direction==0:
        next_x, next_y=x+1, y
    elif direction==1:
        next_x, next_y=x, y-1
    elif direction==2:
        next_x, next_y=x-1, y
    elif direction==3:
        next_x, next_y=x, y+1
    if 0< next_x<n-1 and 0< next_y<m-1: # 양 끝 벽 뺌
        if graph[next_x][next_y]!=1:
            return next_x, next_y, direction

    return -1,-1,-1 # 작동을 멈춤
cnt=0
while True:
    if graph[robot_x][robot_y] ==0 :
        graph[robot_x][robot_y]=2 # 청소하기
        cnt+=1

    robot_x, robot_y, direction= search_next(robot_x, robot_y,direction)

    if robot_x==-1:
        break
print(cnt)
