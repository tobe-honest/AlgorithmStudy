import sys
input = sys.stdin.readline

def search(left, right):
    mid = (left + right) // 2
    # while left <= right:
    #     compare = 

N, C = map(int, input().split())
coordinate = [int(input()) for i in range(N)]
coordinate.sort()
