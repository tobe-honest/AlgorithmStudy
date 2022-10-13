def weight(rope, N):
    k = 0
    res = 0
    weight = 0
    for ro in rope:
        weight += ro
        k += 1
        tmp = min((weight // k), ro)
        if res <= tmp * k:
            res = tmp * k
    print(res)

if __name__ == '__main__':
    N = int(input())
    rope = [int(input()) for _ in range(N)]
    rope.sort(reverse=True)
    weight(rope, N)