import sys

def line():
    m_val = 0
    for i in range(N):
        for j in range(M-3):
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            m_val = max(val,m_val)
    
    for j in range(M):
        for i in range(N-3):
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
            m_val = max(val,m_val)

    return m_val

def square():
    m_val = 0
    for i in range(N-1):
        for j in range(M-1):
            val = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            m_val = max(val,m_val)
    
    return m_val


def uoo(): 
    m_val = 0
    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i+1][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i+1][j+1] + board[i][j] + board[i+1][j] + board[i+2][j]
            m_val = max(val,m_val)

    return m_val

def R():
    m_val = 0
    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
            m_val = max(val,m_val)


    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j+1] + board[i][j+2] + board[i+1][j+1] + board[i+1][j]
            m_val = max(val,m_val)

    return m_val

def G():
    m_val = 0
    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            m_val = max(val,m_val)

    for i in range(N-2):
        for j in range(M-1):
            val = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i+1][j+2] + board[i][j] + board[i][j+1] + board[i][j+2]
            m_val = max(val,m_val)

    for i in range(N-1):
        for j in range(M-2):
            val = board[i+1][j] + board[i][j] + board[i][j+1] + board[i][j+2]
            m_val = max(val,m_val)

    return m_val

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

print(max(line(),square(),uoo(),R(),G()))