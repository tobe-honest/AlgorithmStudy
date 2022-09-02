import sys
input = sys.stdin.readline

def recersive(x, y, n):
    global cnt
    num = arr[x][y]
    mid = n // 3

    for i in range(x, x + n):
        for j in range(y, y + n):
            if num != arr[i][j]:
                recersive(x, y, mid)
                recersive(x, y + mid, mid)
                recersive(x, y + mid*2, mid)
                
                recersive(x + mid, y, mid)
                recersive(x + mid, y + mid, mid)
                recersive(x + mid, y + mid*2, mid)

                recersive(x + mid*2, y, mid)
                recersive(x + mid*2, y + mid, mid)
                recersive(x + mid*2, y + mid*2, mid)

                return
    cnt[num] += 1

n = int(input())
cnt = [0] * 3
arr = [list(map(int, input().split())) for _ in range(n)]

recersive(0, 0, n)

# cnt에 0 -> 1 -> -1 순서로 저장됨
print(cnt[2])
print(cnt[0])
print(cnt[1])