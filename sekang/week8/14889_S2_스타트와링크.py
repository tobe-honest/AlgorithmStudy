from itertools import combinations

def find():
    diff = int(1e9)
    l = set([i for i in range(N)])
    for A in combi:
        B = list(l - set(A))
        total_B = 0
        total_A = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                total_A += S[A[i]][A[j]] + S[A[j]][A[i]]
                total_B += S[B[i]][B[j]] + S[B[j]][B[i]]
        if diff > abs(total_A - total_B):
            diff = abs(total_A - total_B)
        # print(A, B, diff)
    print(diff)

if __name__ == '__main__':
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    combi = list(combinations([i for i in range(N)], N//2))
    find()
