# BaekJoon P14888 "연산자 끼워넣기" (전수조사, 백트레킹 | S1)
"""
---[실수]---
max 초기값 설정 시 0으로 설정
-> max가 음수일 수도 있음 => max_case = -float('inf')
---[부족한 점]---
생각을 깊게 안함 => permutations 사용 -> 너무 오래걸림, case가 더 컸으면 시간초과
또한 permutations는 중복되는 값들 또한 search 하기에 비효율적
---[풀이]---
모든 경우에 대해서 dfs 실시
+, - , * , / 에 대해 남은 개수에 맞게 뿌리를 뻗어나가는 것
모든 연산자를 사용한 후 나온 결과를 계속해서 비교하여
최대값과 최소값을 구함
---[비고]---
풀이 시간 : 30m
permutations -> 메모리 : 30840 | 시간 : 7968
dfs -> 메모리: 30840 | 시간 : 100
"""
import sys
from itertools import permutations


def calc(ops, nums):
    result = nums[0]
    for op, num in zip(ops, nums[1:]):
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        else:
            if result < 0:
                temp = -result // num
                result = -temp
            else:
                result //= num

    return result


def solution(nums, operations):
    op_result = []
    op_result.extend(['+'] * operations[0])
    op_result.extend(['-'] * operations[1])
    op_result.extend(['*'] * operations[2])
    op_result.extend(['/'] * operations[3])
    min_case = float('inf')
    max_case = -float('inf')
    for ops in permutations(op_result):
        result = calc(ops, nums)
        max_case = max(max_case, result)
        min_case = min(min_case, result)

    return max_case, min_case


def calc2(answer, n, nums, result, idx, op_temp):
    if idx == n:
        max_case = answer[0]
        min_case = answer[1]
        answer[0] = max(max_case, result)
        answer[1] = min(min_case, result)
        return

    plus, minus, multiply, divide = op_temp
    if plus > 0:
        calc2(answer, n, nums, result + nums[idx], idx + 1, [plus - 1, minus, multiply, divide])
    if minus > 0:
        calc2(answer, n, nums, result - nums[idx], idx + 1, [plus, minus - 1, multiply, divide])
    if multiply > 0:
        calc2(answer, n, nums, result * nums[idx], idx + 1, [plus, minus, multiply - 1, divide])
    if divide > 0:
        if result < 0:
            temp = -result // nums[idx]
            calc2(answer, n, nums, -temp, idx + 1, [plus, minus, multiply, divide - 1])
        else:
            calc2(answer, n, nums, result // nums[idx], idx + 1, [plus, minus, multiply, divide - 1])


def solution2(n, nums, operations):
    min_val = float('inf')
    max_val = -float('inf')
    answer = [max_val, min_val]
    calc2(answer, n, nums, nums[0], 1, operations)

    return answer


if __name__ == '__main__':
    N = int(input())
    inputs1 = [*map(int, sys.stdin.readline().split())]
    inputs2 = [*map(int, sys.stdin.readline().split())]
    print(*solution2(N, inputs1, inputs2), sep='\n')
