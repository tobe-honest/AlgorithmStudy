
def check(x, y):
    return True if 0 <= x < N and 0 <= y < M else False

def back_xy(x, y, dir):
    if dir == 0 or dir == 1:
        nx, ny = x + dx[dir + 2], y + dy[dir + 2]
    else:
        nx, ny = x + dx[dir - 2], y + dy[dir - 2]
    return nx, ny

def bfs(gmap, visited, x, y, dir):
    # 탈출 조건 (벽, 이미 방문, 범위 벗어남)
    global cnt

    while True:
        unavail = 0 # 이동 불가 판단 flag
        for _ in range(4):
            nx, ny = x + dx[(dir - 1) % 4], y + dy[(dir - 1) % 4]

            # 청소 가능 조건 -> 이동 가능한 구역이 하나라도 있는 경우
            if check(nx, ny) and not visited[nx][ny] and gmap[nx][ny] != 1:
                dir = (dir - 1) % 4
                visited[nx][ny] = True
                x, y = nx, ny
                cnt += 1
                unavail = 1
                break
            else:
                dir = (dir - 1) % 4

        if unavail == 0: # 이동 불가 -> 후진
            r, c = back_xy(x, y, dir)
            if gmap[r][c] == 1: # 뒤가 벽인 경우
                break
            else:
                x, y = r, c

if __name__ == '__main__':
    N, M = map(int, input().split())  # x, y
    x, y, dir = map(int, input().split())  # 0:북, 1:동, 2:남, 3:서
    gmap = [list(map(int, input().split())) for _ in range(N)]  # 0:빈 칸, 1:벽
    visited = [[False] * M for _ in range(N)]  # 청소 여부(= 방문 여부)
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited[x][y] = True
    cnt = 1 # 현재 위치는 항상 청소 가능
    bfs(gmap, visited, x, y, dir)

    print(cnt)
