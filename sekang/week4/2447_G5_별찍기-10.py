import sys
sys.setrecursionlimit(10000)

def recursive(star, x, y, N, flag):
    
    step = N//3
    
    if N == 3:
        if flag == 4:
            for i in range(x, x + N):
                for j in range(y, y + N):
                    star[i][j] = ' '
        else:
            star[x+1][y+1] = ' '
        return

    else:
        if flag == 4:
            for i in range(x, x + N):
                for j in range(y, y + N):
                    star[i][j] = ' '
            return

    recursive(star, x, y, step, 0)
    recursive(star, x, y + step, step, 1)
    recursive(star, x, y + step * 2, step, 2)

    recursive(star, x + step, y, step, 3)
    recursive(star, x + step, y + step, step, 4)
    recursive(star, x + step, y + step * 2, step, 5)

    recursive(star, x + step * 2, y, step, 6)
    recursive(star, x + step * 2, y + step, step, 7)
    recursive(star, x + step * 2, y + step * 2, step, 8)

N = int(input())
star = [['*'] * N for _ in range(N)]
recursive(star, 0, 0, N, 0)

for i in range(N):
    for j in range(N):
        print(star[i][j], end="")
    print()

# for s in star:
#     print(s)