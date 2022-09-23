import sys

def check(tree):
    start, end= 0, tree[-1]

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for t in tree:
            if t > mid:
                cnt += t - mid

        if cnt == M:
            return mid
        elif cnt > M:
            start = mid + 1
        else:
            end = mid - 1

    return end
    
N,M = map(int,input().split())
tree = list(map(int,sys.stdin.readline().split()))
tree.sort()
print(check(tree))