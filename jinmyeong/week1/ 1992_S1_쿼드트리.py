import sys
input = sys.stdin.readline
result = ''

def search(x, y, N):
    global result
    if N == 1:
        for i in range(x, x+N):
            for j in range(y, y+N):
                result += board[i][j]
        return

    summation = sum([int(board[i][j]) for i in range(x, x+N) for j in range(y, y+N)])
    if not summation:
        result += '0'
        return
    elif summation == N*N: 
        result += '1'
        return
    else:
        result += '('
        search(x, y, N//2)
        search(x, y+N//2, N//2)
        search(x+N//2, y, N//2)
        search(x+N//2, y+N//2, N//2)
        result += ')'


N = int(input())
board = [list(input().strip()) for i in range(N)]
search(0,0,N)
print(result)