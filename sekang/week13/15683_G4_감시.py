from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

Dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 1], [2, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def print_gmap(gmap):
    for g in gmap:
        print(g)
    print()
    print()

def look(x, y, Dir, temp):
    for dir in Dir:
        nx, ny = x, y
        while True:
            nx += dx[dir]
            ny += dy[dir]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] != 6:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
            else:
                break

def dfs(gmap, cnt):
    # temp = deepcopy(gmap)

    if cnt == num:
        temp = [g[:] for g in gmap]
        global answer
        total = 0
        for tmp in temp:
            total += tmp.count(0)
        answer = min(answer, total)
        return

    x, y, cctv = camera[cnt]
    for D in Dir[cctv]:
        temp = [g[:] for g in gmap]
        look(x, y, D, temp)
        dfs(temp, cnt + 1)
        
        # temp = deepcopy(gmap)
        # print_gmap(temp)
    
if __name__ == '__main__':
    n, m = map(int, input().split())
    gmap = [list(map(int, input().split())) for _ in range(n)]
    camera = []
    answer = 1e9
    num = 0

    for i in range(n):
        for j in range(m):
            if 1 <= gmap[i][j] <= 5:
                camera.append((i, j, gmap[i][j]))
                num += 1
    
    # print(camera)

    dfs(gmap, 0)
    print(answer)