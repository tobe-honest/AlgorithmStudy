import sys
sys.setrecursionlimit(100000000)
input = sys.stdin.readline

def travel(lst, parent, child):
    if not rank[child]:
        rank[child] = parent
        for ch in lst[child]:
            travel(lst, child, ch)
    return


if __name__ == '__main__':
    n = int(input())
    lst = [[] for _ in range(n + 1)]
    rank = [0] * (n + 1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    for child in lst[1]:
        travel(lst, 1, child)
    
    for ra in rank[2:]:
        print(ra)