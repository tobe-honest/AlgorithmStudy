from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    visit = [[0 for j in range(M)] for i in range(N)]
    queue = deque([[i,j,0]])
    visit[i][j] = True
    m_level = 0
    while queue:
        y,x,level = queue.popleft()
        if m_level < level:
            m_level = level
        for i in range(4):
            ky,kx = y + dy[i] , x + dx[i]
            if ky<0 or kx <0 or ky >= N or kx >= M or visit[ky][kx] == True or board[ky][kx] == 'W':
                continue
            visit[ky][kx] = True
            queue.append([ky,kx,level+1])
            
    return m_level


N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(input()))

can = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            can.append([i,j])

m_val = 0
for i in range(len(can)):
    val = bfs(can[i][0],can[i][1])
    if m_val < val:
        m_val = val

print(m_val)