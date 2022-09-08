import sys
input = sys.stdin.readline

def recursive(x, y, n):
    
    global cnt

    if x == r and y == c:
        print(cnt)
        return
    
    half = n // 2

    if x <= r < x + half and y <= c < y + half:
        # print(0, cnt)
        recursive(x, y, half)
    
    elif x <= r < x + half and y + half <= c < y + n:
        cnt += (half ** 2) * 1
        # print(1, cnt)
        recursive(x, y + half, half)

    elif x + half <= r < x + n and y <= c < y + half:
        cnt += (half ** 2) * 2
        # print(2, cnt)
        recursive(x + half, y, half)
    
    elif x + half <= r < x + n and y + half <= c < y + n:
        cnt += (half ** 2) * 3
        # print(3, cnt)
        recursive(x + half, y + half, half)

n, r, c = map(int, input().split())
cnt = 0

recursive(0, 0, 2 ** n) # n은 한변의 길이