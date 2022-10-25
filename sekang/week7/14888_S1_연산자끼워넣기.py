from itertools import permutations

def solve(num, op):

    result = []
    for o in op:
        # print(o)
        tmp = [n for n in num]
        for k in range(len(o)):
            # print(tmp)
            if o[k] == 1:
                tmp[k + 1] = tmp[k] + tmp[k + 1]
            elif o[k] == 2:
                tmp[k + 1] = tmp[k] - tmp[k + 1]
            elif o[k] == 3:
                tmp[k + 1] = tmp[k] * tmp[k + 1]
            else:
                if tmp[k] < 0 and tmp[k + 1] > 0:
                    tmp[k + 1] = -(abs(tmp[k]) // tmp[k + 1])
                else:
                    tmp[k + 1] = tmp[k] // tmp[k + 1]
            # print(op[k])
        result.append(tmp[-1])
        # print(tmp)

    result.sort()
    # print(result)
    print(result[-1])
    print(result[0])

def gen_permutations(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for P in gen_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]

    return result

if __name__ == '__main__':
    N = int(input())
    num = list(map(int, input().split()))
    op_list = list(map(int, input().split()))
    tmp = [1, 2, 3, 4]
    op = [tmp[i] for i in range(4) for j in range(op_list[i]) if op_list[i] != 0]

    # print(op)
    # print(gen_permutations(op, N-1))
    # op = gen_permutations(op, N-1)
    op = list(permutations(op, N-1))
    # print(op)
    solve(num, op)
