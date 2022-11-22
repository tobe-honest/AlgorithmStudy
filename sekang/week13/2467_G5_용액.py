import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    solution = list(map(int, input().split()))
    answer = 2e9
    i = 0
    j = n - 1
    while i < j:

        total = solution[i] + solution[j]
        
        if answer > abs(total):
            answer = abs(total)
            l = [solution[i], solution[j]]
        
        if total == 0:
            break
        elif total > 0:
            j -= 1
        else:
            i += 1

    print(l[0], l[1])