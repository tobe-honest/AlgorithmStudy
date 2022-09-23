n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
    data[i] = max(data[i], data[i] + data[i-1])

print(max(data))