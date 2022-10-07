from collections import deque

def bfs(visited):
    queue = deque() # disp, clip의 이모티콘 수
    queue.append((1, 0, 0))
    visited[1][0] = True # 걸린 시간

    while queue:
        screen, clipboard, cnt = queue.popleft()

        if screen == S:
            print(cnt) # 이동 횟수
            return

        for i in range(3):
            if i == 0: # case 1
                new_clipboard, new_screen = screen, screen
            elif i == 1: # case 2
                new_screen, new_clipboard = screen + clipboard, clipboard
            else: # case 3
                new_screen, new_clipboard = screen - 1, clipboard

            # 범위 체크 + 최소 이동 횟수니까 방문한 지점은 피해서
            if 0 <= new_screen < S+1 and 0 <= new_clipboard < S+1 and not visited[new_screen][new_clipboard]:
                visited[new_screen][new_clipboard] = True
                queue.append((new_screen, new_clipboard, cnt + 1))
        
        # print(queue)

S = int(input())
visited = [[False] * (S+1) for _ in range(S+1)]

bfs(visited)

# for v in visited:
#     print(v)
