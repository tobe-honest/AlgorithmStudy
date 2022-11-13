from copy import deepcopy

def move(board, dir):
    if dir == 0: # 동 (동에서 서로 이동)
        for i in range(n):
            top = n - 1
            for j in range(n-2, -1, -1):
                if board[i][j]: # 0이면 pass
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0: # 단순 이동
                        board[i][top] = tmp
                    elif board[i][top] == tmp: # 숫자 합치기
                        board[i][top] = tmp * 2
                        top -= 1 
                    else: # 숫자가 다르면 해당 위치 서로 이동
                        top -= 1
                        board[i][top] = tmp
                        
    elif dir == 1: # 서 (서에서 동으로 이동)
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]: # 0이면 pass 
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0: # 단순 이동
                        board[i][top] = tmp
                    elif board[i][top] == tmp: # 숫자 합치기
                        board[i][top] = tmp * 2
                        top += 1
                    else: # 숫자가 다르면 해당 위치 우로 이동
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남 (남에서 북으로 이동)
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]: # 0이면 pass 
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:  # 단순 이동
                        board[top][j] = tmp
                    elif board[top][j] == tmp: # 숫자 합치기
                        board[top][j] = tmp * 2
                        top -= 1
                    else: # 숫자가 다르면 해당 위치 위로 이동
                        top -= 1
                        board[top][j] = tmp

    else: # 북 (북에서 남으로 이동)
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]: # 0이면 pass 
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0: # 단순 이동
                        board[top][j] = tmp
                    elif board[top][j] == tmp: # 숫자 합치기
                        board[top][j] = tmp * 2
                        top += 1
                    else: # 숫자가 다르면 해당 위치 아래로 이동
                        top += 1
                        board[top][j] = tmp

    return board

def dfs(board, cnt):
    global result
    if cnt == 5: # 종료 조건
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return

    for i in range(4):
        copy_board = move(deepcopy(board), i)
        dfs(copy_board, cnt + 1)

if __name__ == '__main__':
    n = int(input()) # 보드의 크기
    board = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    dfs(board, 0)
    print(result)