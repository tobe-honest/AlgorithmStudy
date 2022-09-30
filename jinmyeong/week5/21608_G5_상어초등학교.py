from collections import deque
input=__import__("sys").stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_position(x, y):
    return 0 <= x < N and 0 <= y < N

def check_possible(x, y, stud_no):
    cnt = 0
    cnt_love = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if check_position(nx, ny): 
            if not board[nx][ny]: cnt += 1
            if diction[stud_no][board[nx][ny]]:
                cnt_love += 1
    return cnt, cnt_love

def make_candidate(board, stud_no):
    candidate = []
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                cnt, cnt_love = check_possible(i, j, stud_no)
                candidate.append((cnt_love, cnt, i, j))
  
    return sorted(candidate, key = lambda x: (-x[0], -x[1], x[2], x[3]))[0]

if __name__ == "__main__":
    N = int(input())
    diction = dict()
    student = list()
    board = [[0 for j in range(N)] for i in range(N)]

    for i in range(N**2):
        n, *l = list(map(int, input().split()))
        student.append(n)
        t = [0 for i in range(N**2+1)]
        for i in range(4):
            t[l[i]] = 1
        diction[n] = t
    for stud_no in range(N**2):
        c_l, c, i, j = make_candidate(board, student[stud_no])
        board[i][j] = student[stud_no]
    is_good = {0 : 0, 1 : 1, 2 : 10, 3 : 100, 4 : 1000}
    result=0
    for i in range(N):
            for j in range(N):
                _, cnt_love = check_possible(i, j, board[i][j])
                result += is_good[cnt_love]
    print(result)