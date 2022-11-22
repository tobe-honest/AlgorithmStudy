from itertools import product
import sys
import copy

def up(board,N):
    for j in range(N):
        p = 0
        for i in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[p][j] == 0:
                    board[p][j] = tmp
                elif board[p][j]  == tmp:
                    board[p][j] *= 2
                    p += 1
                else:
                    p += 1
                    board[p][j] = tmp

    return board

def down(board,N):
    for j in range(N):
        p = N - 1
        for i in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[p][j] == 0:
                    board[p][j] = tmp
                elif board[p][j]  == tmp:
                    board[p][j] *= 2
                    p -= 1
                else:
                    p -= 1
                    board[p][j] = tmp
    return board

def left(board,N):
    for i in range(N):
        p = 0
        for j in range(1, N):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][p] == 0:
                    board[i][p] = tmp
                elif board[i][p]  == tmp:
                    board[i][p] *= 2
                    p += 1
                else:
                    p += 1
                    board[i][p]= tmp
    return board

def right(board,N):
    for i in range(N):
        p = N - 1
        for j in range(N - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][p] == 0:
                    board[i][p] = tmp
                elif board[i][p]  == tmp:
                    board[i][p] *= 2
                    p -= 1
                else:
                    p -= 1
                    board[i][p] = tmp
    return board

def check(case,board,N):
    for d in case:
        if d == 0:
            board = up(board,N)
        elif d == 1:
            board = left(board,N)
        elif d == 2:
            board = down(board,N)
        elif d == 3:
            board = right(board,N)

    return max(map(max, board))


def solution(N,board):
    cases = []
    for i in product(range(4), range(4), range(4), range(4), range(4)):
        cases.append(i)

    m_val = 0
    for case in cases:
        val = check(case,copy.deepcopy(board),N)
        if m_val < val:
            m_val = val

    return m_val

if __name__=="__main__":
    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int,sys.stdin.readline().split())))
    print(solution(N, board))