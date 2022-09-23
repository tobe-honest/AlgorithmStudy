import heapq
import sys
input = sys.stdin.readline

def find(heap):
    time = []
    start, end = heapq.heappop(heap)
    heapq.heappush(time, end)

    while heap:
        start, end = heapq.heappop(heap)
        if time[0] <= start: # 끝나는 시간이랑 시작 시간 비교
            heapq.heappop(time)
        heapq.heappush(time, end)
        print(time)

    # print(len(time))
    return

N = int(input())
heap = []
for i in range(N):
    num, start, end = map(int, input().split())
    heapq.heappush(heap, (start, end))
find(heap)

# while heap:
#     print(heapq.heappop(heap))
# print()