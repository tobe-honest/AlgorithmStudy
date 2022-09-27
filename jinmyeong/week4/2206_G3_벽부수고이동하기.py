from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def search(start, graph):
    visited = [[[0, 0] for j in range(M)] for i in range(N)]
    visited[start[0]][start[1]][0] = 1
    q = deque([start])
    while q:
        x, y, is_break = q.popleft()
        
        # 방문 했으면 바로 끝내
        if x == N-1 and y == M-1: return visited[x][y][is_break]

        # 4방 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 범위 안에 있으면 일단 보자
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 없는곳 + 아직 방문 안했어?
                # 그럼 방문하고 현재 위치 + 1 값을 해당 위치에 넣어
                if graph[nx][ny] == '0' and not visited[nx][ny][is_break]:
                    visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                    q.append((nx, ny, is_break))

                # 벽이 있는데 아직 부순적이 없어?
                # 그럼 해당 위치에 부쉈다는 부분에 현재위치 + 1 값 넣어
                # 그리고 is_break 부쉈다고 바꿔
                elif graph[nx][ny] == '1' and not is_break:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
    return -1

if __name__ == "__main__":
    N, M = map(int, input().split())
    l = [list(input().strip()) for i in range(N)]
    print( search((0,0,0), l) )
