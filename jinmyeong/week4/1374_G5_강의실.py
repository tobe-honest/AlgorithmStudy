import heapq
import sys
input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for i in range(N)]

l = sorted(l, key = lambda x : (x[1], x[2]))
h = [l[0][2]]
heapq.heapify(h)

for i in range(1, N):
    compare = heapq.heappop(h)
    if compare > l[i][1]:
        heapq.heappush(h, compare)
        heapq.heappush(h, l[i][2])
    else:
        heapq.heappush(h, l[i][2])

print(len(h))