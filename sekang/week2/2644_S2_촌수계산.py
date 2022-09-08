from collections import deque

def bfs(start, end):
    cnt = 0
    queue = deque()
    queue.append((cnt, start))

    while queue:
        cnt, present = queue.popleft()

        if present == end:
            print(cnt)
            return

        for i in range(m):
            x, y = data[i][0], data[i][1]

            if x == present and not visited[i]:
                queue.append((cnt+1, y))
                visited[i] = True
            elif y == present and not visited[i]:
                queue.append((cnt+1, x))
                visited[i] = True
    print(-1)
    return

n = int(input())
a, b = map(int, input().split())
m = int(input())
data = [list(map(int, input().split())) for _ in range(m)] # 부모-자식
visited = [False] * m

bfs(a, b)