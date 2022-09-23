import sys
input = sys.stdin.readline

# 조합
def ncr(row, col, n, cnt):
    # 현재 [row, col]이 [r, C]와 같으면 출력 후 종료
    if r == row and C == col:
        print(cnt)
        exit()
    # n이 1이라면 (최소로 분할 했다면)
    # cnt ++
    if n == 1:
        cnt += 1
        return cnt
    # 현재 row와 col을 기준으로 n x n 범위에
    # r과 C가 존재하면 재귀
    # 범위 안에 없으면 n*n만큼 cnt증가
    if row <= r < row + n and col <= C < col + n:
        cnt = ncr(row, col, n//2, cnt)
        cnt = ncr(row, col + n//2, n//2, cnt)
        cnt = ncr(row + n//2, col, n//2, cnt)
        cnt = ncr(row + n//2, col + n//2, n//2, cnt)
    else:
        cnt += n * n
        return cnt

if __name__ == '__main__':
    cnt = 0
    N, r, C = map(int,input().split())
    ncr(0, 0, 2**(N), cnt)