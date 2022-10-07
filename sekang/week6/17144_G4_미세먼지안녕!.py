def check(x, y): # 범위와 공기청정기 있는지 확인
    return True if 0 <= x < R and 0 <= y < C and gmap[x][y] != -1 else False

def spread():
    arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if gmap[i][j] > 0:
                tmp = 0
                if check(i-1, j):
                    arr[i-1][j] += gmap[i][j] // 5
                    tmp += gmap[i][j] // 5
                if check(i+1, j):
                    arr[i+1][j] += gmap[i][j] // 5
                    tmp += gmap[i][j] // 5
                if check(i, j-1):
                    arr[i][j-1] += gmap[i][j] // 5
                    tmp += gmap[i][j] // 5
                if check(i, j+1):
                    arr[i][j+1] += gmap[i][j] // 5
                    tmp += gmap[i][j] // 5
                gmap[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            gmap[i][j] += arr[i][j]
    
def air_move(arr, up, down):
    # up
    # 1 - 아래
    temp = arr[up[0]][C - 1]
    for i in range(C - 1, 1, - 1):
        arr[up[0]][i] = arr[up[0]][i - 1]
    arr[up[0]][1] = 0

    # 2 - 오른쪽
    temp_1 = arr[0][C - 1]
    for i in range(up[0] - 1):
        arr[i][C - 1] = arr[i + 1][C - 1]
    arr[up[0] - 1][C - 1] = temp

    # 3 - 위쪽
    temp_2 = arr[0][0]
    for i in range(C - 2):
        arr[0][i] = arr[0][i + 1]
    arr[0][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(up[0] - 1, 1, -1):
        arr[i][0] = arr[i - 1][0]
    arr[1][0] = temp_2

    # down
    # 1- 위쪽
    temp = arr[down[0]][C - 1]
    for i in range(C - 1, 1, -1):
        arr[down[0]][i] = arr[down[0]][i - 1]
    arr[down[0]][1] = 0

    # 2 오른쪽
    temp_1 = arr[R - 1][C - 1]
    for i in range(R - 1, down[0] + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    arr[down[0] + 1][C - 1] = temp

    # 3 - 아래쪽
    temp_2 = arr[R - 1][0]
    for i in range(C - 2):
        arr[R - 1][i] = arr[R - 1][i + 1]
    arr[R - 1][C - 2] = temp_1

    # 4 - 왼쪽
    for i in range(down[0] + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[R - 2][0] = temp_2

def find():

    air1_x = air[0] # 2
    air2_x = air[1] # 3
    time = 0
    while time != T:
        spread() # step 1
        air_move(gmap, [air[0], 0], [air[1], 0])
        time += 1

    # print(gmap)

    total = sum([gmap[i][j] for i in range(R) for j in range(C) if gmap[i][j] > 0])
    print(total)
    return

R, C, T = map(int, input().split())
gmap = [list(map(int, input().split())) for _ in range(R)]

air = [i for i in range(2, R-2) if gmap[i][0] == -1]
find()