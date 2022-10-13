from copy import deepcopy

def check(x, y):
    return  True if 0 <= x < 4 and 0 <= y < 4 else False

def dfs(graph, score, x, y):
    global max_score
    score += graph[x][y][0]
    max_score = max(max_score, score)
    graph[x][y][0] = 0 # 해당 지점 초기화

    # 물고기 이동
    for fish in range(1, 17): # 1~16
        fish_x = fish_y = -1
        # i번째 위치 찾기
        for i in range(4):
            for j in range(4):
                if graph[i][j][0] == fish:
                    fish_x, fish_y = i, j
                    break
        if fish_x == fish_y == -1:
            continue
        f_dir = graph[fish_x][fish_y][1] # 방향

        for k in range(8):
            idx = (f_dir + k) % 8
            nx = fish_x + dx[idx]
            ny = fish_y + dy[idx]
            # 범위를 나가거나 상어가 있는 위치면 안감
            if not check(nx, ny) or (nx == x and ny == y):
                continue
            graph[fish_x][fish_y][1] = idx # 방향 변경
            graph[fish_x][fish_y], graph[nx][ny] = graph[nx][ny], graph[fish_x][fish_y] # 위치 교환
            break

    # 상어 먹음
    s_dir = graph[x][y][1]
    for t in range(1, 5): # 1~4
        nx = x + dx[s_dir] * t
        ny = y + dy[s_dir] * t
        if check(nx, ny) and graph[nx][ny][0] > 0:
            dfs(deepcopy(graph), score, nx, ny)


if __name__ == '__main__':
    graph = [[] for _ in range(4)]
    max_score = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        tmp = []
        info = list(map(int, input().split()))
        for j in range(4):
            tmp.append([info[j*2], info[j*2+1]-1])
        graph[i] = tmp
    # print(graph)
    dfs(graph, 0, 0, 0)
    print(max_score)