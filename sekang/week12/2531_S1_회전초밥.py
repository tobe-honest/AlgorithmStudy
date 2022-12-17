import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, d, k, c = map(int, input().split())
    
    dish = [int(input()) for _ in range(n)]
    dish += dish[:k-1]
    answer = 0
    for i in range(n):
        S = set(dish[i:i+k])
        # print(S)
        tmp = len(S) + 1 if c not in S else len(S)
        answer = max(answer, tmp)
    print(answer)