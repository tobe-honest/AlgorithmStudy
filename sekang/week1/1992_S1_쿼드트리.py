def recursive(x, y, n):
    
    img = arr[x][y]
    half = n // 2

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != img:
                print('(', end="")
                recursive(x, y, half)
                recursive(x, y + half, half)
                recursive(x + half, y, half)
                recursive(x + half, y + half, half)
                print(')', end="")
                return
            
    return print(img, end="")

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

recursive(0, 0, n)
