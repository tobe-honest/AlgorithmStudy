import sys
input = sys.stdin.readline

# 상 하 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, total, cnt): # 4번 움직여서 갈 수 있는 경우가 방향키 모양 빼고 포함됨
    global result
    # global ccnt
    if cnt == 4: # 4개 선택한 경우 == 모양이 결정됨
        result = max(result, total)
        return 

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # ccnt += 1
            visited[nx][ny] = True
            dfs(nx, ny, total + board[nx][ny], cnt + 1)
            visited[nx][ny] = False

def find_arrow_keys(i, j):
    global result
    # global ccnt
    for k in range(4):
        total = board[i][j]
        for t in range(3): # 상하좌(9시), 하좌우(6시), 좌우상(12시), 우상하(3시)
            idx = (k+t) % 4
            nx, ny = i + dx[idx], j + dy[idx]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                total = 0
                break
            # ccnt += 1
            total += board[nx][ny]
        result = max(result, total)
    return

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    
    result = 0
    # ccnt = 0
    for i in range(n):
        for j in range(m):        
            visited[i][j] = True
            dfs(i, j, board[i][j], 1)
            visited[i][j] = False
            find_arrow_keys(i, j)
            
    # print(ccnt)
    print(result)