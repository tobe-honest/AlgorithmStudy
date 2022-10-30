from collections import deque

def check(x, y):
    return True if 0 <= x < r and 0 <= y < c else False

def bfs():
    result = 0
    queue = deque()
    for x, y in ij:
        cnt = 0
        visited = [[0] * c for _ in range(r)]
        visited[x][y] = 1
        queue.append((x, y))
        while queue:
            nx, ny = queue.popleft()
            cnt = max(visited[nx][ny]-1, cnt)

            if check(nx-1, ny) and not visited[nx-1][ny] and gmap[nx-1][ny]:
                visited[nx-1][ny] = visited[nx][ny] + 1
                queue.append((nx-1, ny))

            if check(nx+1, ny) and not visited[nx+1][ny] and gmap[nx+1][ny]:
                visited[nx+1][ny] = visited[nx][ny] + 1
                queue.append((nx+1, ny))

            if check(nx, ny-1) and not visited[nx][ny-1] and gmap[nx][ny-1]:
                visited[nx][ny-1] = visited[nx][ny] + 1
                queue.append((nx, ny-1))

            if check(nx, ny+1) and not visited[nx][ny+1] and gmap[nx][ny+1]:
                visited[nx][ny+1] = visited[nx][ny] + 1
                queue.append((nx, ny+1))

        result = max(result, cnt)
    print(result)
    return

if __name__ == '__main__':
    r, c = map(int, input().split())
    gmap = []
    ij = []
    for i in range(r):
        tmp = []
        string = input()
        for j in range(len(string)):
            if string[j] == 'W': # 이동 X
                tmp.append(0)
            else: # 이동 O
                ij.append((i, j))
                tmp.append(1)
        gmap.append(tmp)
    # print(ij)
    bfs() # 거리가 먼 지점 사이 최단 거리 찾기