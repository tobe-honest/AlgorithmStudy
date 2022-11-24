import sys
import copy

dx = [1,0,-1,0]
dy = [0,-1,0,1]

mode = [    
            [[]],
            [[0],[1],[2],[3]],
            [[0,2],[1,3]],
            [[0,1],[1,2],[2,3],[3,0]],
            [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
            [[0,1,2,3]]
        ]


def observe(board,ds,y,x):
    for d in ds:
        ky,kx = y,x
        while True:
            ky,kx = ky+dy[d], kx+dx[d]
            if ky<0 or kx<0 or ky>=n or kx >= m or board[ky][kx] == 6:
                break
            if board[ky][kx] == 0:
                board[ky][kx] = 7


def solution(board,depth):
    global min_value

    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += board[i].count(0)
        min_value = min(min_value,cnt)
        return

    y,x,num = cctv[depth]

    for ds in mode[num]:
        temp = copy.deepcopy(board)
        observe(temp,ds,y,x)
        solution(temp,depth+1)

if __name__ == "__main__":
    n,m = map(int,sys.stdin.readline().split())

    board, cctv = [], []
    for i in range(n):
        line = list(map(int,sys.stdin.readline().split()))
        board.append(line)
        for j in range(m):
            if 0 < line[j] < 6:
                cctv.append([i,j,line[j]])
    
    min_value = 64
    solution(board,0)
    print(min_value)