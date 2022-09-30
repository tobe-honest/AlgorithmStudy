from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def search(l, start, visited, cnt, mode="normal"):
    q = deque([start])
    visited[start[0]][start[1]] = True
    check = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if cx >= 0 and cx < N and cy >= 0 and cy < N and not visited[cx][cy]:
                if mode=="normal":
                    if l[start[0]][start[1]] == l[cx][cy]:
                        visited[cx][cy] = True
                        q.append((cx, cy))
                        check += 1
                else:
                    if l[start[0]][start[1]] == "B":
                        if l[start[0]][start[1]] == l[cx][cy]:
                            visited[cx][cy] = True
                            q.append((cx, cy))
                            check += 1
                    else:
                        if l[cx][cy] != "B":
                            visited[cx][cy] = True
                            q.append((cx, cy))
                            check += 1

                    
    return cnt + 1 #if check else cnt
    


if __name__ == "__main__":
    N = int(input())
    l = [list(input().strip()) for i in range(N)]
    visited = [[False for j in range(N)] for i in range(N)]
    visited2 = [[False for j in range(N)] for i in range(N)]
    cnt1, cnt2 = 0, 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt1 = search(l, (i, j), visited, cnt1, "normal")
            if not visited2[i][j]:
                cnt2 = search(l, (i, j), visited2, cnt2, "annomal")
    print(cnt1, cnt2)
    