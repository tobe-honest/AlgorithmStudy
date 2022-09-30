from collections import deque
def bfs(cnt, X, visited):
    flag = 1
    queue = deque()
    queue.append((cnt, X))
    while queue:
        cnt, X =queue.popleft()
        if X == K:
            for count, x in queue:
                if count == cnt and x == X:
                    flag += 1
            print(cnt)
            print(flag)
            return

        visited[X] = True
        if 0 <= X + 1 <= 100000 and not visited[X+1]:
            queue.append((cnt + 1, X + 1))
        if 0 <= X - 1 <= 100000 and not visited[X-1]:
            queue.append((cnt + 1, X - 1))
        if 0 <= X * 2 <= 100000 and not visited[X*2]:
            queue.append((cnt + 1, X * 2))
        # visited[X] = True

N, K = map(int, input().split())
visited = [False] * 100001
bfs(0, N, visited)