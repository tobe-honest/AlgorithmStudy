input = __import__("sys").stdin.readline

if __name__ == "__main__":
    K, N = map(int, input().split())
    l = [int(input().strip()) for i in range(K)]
    maximum = 0
    left = 1
    right = max(l)
    while left <= right:
        mid = (left + right) // 2
        s_m = sum([i // mid for i in l])
        if s_m < N:
            right = mid - 1
        else:
            left = mid + 1
            maximum = max(maximum, mid)
    print(maximum)