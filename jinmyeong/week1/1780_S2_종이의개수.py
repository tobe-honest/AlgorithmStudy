import sys
input = sys.stdin.readline

result = [0, 0, 0]
def is_only(l):
    compare = [l[0][0] for i in range(len(l))]
    for i in l:
        if i != compare:
            return 0
    return 1

def search(x, y, N):
    if N == 1:
        if board[x][y] == -1: result[0] += 1
        elif board[x][y] == 0: result[1] += 1
        else: result[2] += 1
        return
    sum_l = [board[i][y:y+N] for i in range(x, x+N)]
    summation = sum([sum([sum(board[i][y:y+N]) for i in range(x, x+N)])])
    if is_only(sum_l):
        if summation == -N*N:
            result[0] += 1
            return
        elif not summation:
            result[1] += 1
            return
        elif summation == N*N:
            result[2] += 1
            return
    else:
        search(x, y, N//3)
        search(x, y + N//3, N//3)
        search(x, y + 2 * N//3, N//3)
        search(x + N//3, y, N//3)
        search(x + N//3, y + N//3, N//3)
        search(x + N//3, y + 2 * N//3, N//3)
        search(x + 2 * N//3, y, N//3)
        search(x + 2 * N//3, y + N//3, N//3)
        search(x + 2 * N//3, y + 2 * N//3, N//3)

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
search(0, 0, N)
print('\n'.join(str(i) for i in result))
