# 바라보는 방향 : 동(0), 북(1), 서(2), 남(3)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

if __name__ == '__main__':
    n = int(input())
    visited = [[False] * 101 for _ in range(101)]

    for _ in range(n):
        x, y, d, g = map(int, input().split())
        mv = [d] # 이동한 방향
        visited[x][y] = True # 방문 위치
        
        for i in range(g): # 세대 범위까지 반복
            temp = [(m + 1) % 4 for m in mv[::-1]]
            # print(mv[::-1])
            # print(mv)
            # print(temp)
            mv += temp
    
        for i in mv:
            nx, ny = x + dx[i], y + dy[i]
            visited[nx][ny] = True
            x, y = nx, ny

    result = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
                result += 1
    
    print(result)