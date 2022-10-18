# BaekJoon P14891 "톱니바퀴" (구현, 시뮬레이션 | G5)
"""
---[실수]---
1. to_move에 현재 바꾸려고 지정된 애를 넣지 않음
2. right에 대한 처리 시, left를 복사해서 left를 right으로 교체해쓴ㄴ데
    left -> right으로 변경하지 않은 부분이 있었음
---[부족한 점]---
---[풀이]---
주어진 K개의 회전방법에 대해서
 각각 먼저 해당 바퀴를 돌렸을 때 영향을 받는 나머지 바퀴들에 대해서 확인한 후
 해당 바퀴들에 대해 rotate 실시

1,2,3,4 의 case를 모두 나누어서 하기보다는
현재 돌리기로 한 바퀴의 양쪽(left, right)으로 판단 진행
돌려야할 바퀴, 방향들에 대해 선정한 후 deque의 rotate를 통해 돌림진행

---[비고]---
풀이 시간 : 50m
메모리: 32524 | 시간 : 96
"""
import sys
from collections import deque


def check(stuff, i, d):

    to_move = [[i, d]]

    # left
    curr_left_val = stuff[i][6]
    curr_direction = d
    left = i - 1
    while left >= 0:
        next_right_val = stuff[left][2]
        # 같이 움질일 바퀴 확인
        if curr_left_val != next_right_val:
            to_move.append([left, -curr_direction])
            curr_left_val = stuff[left][6]
            curr_direction = -curr_direction
            left = left - 1
        else:
            break

    # right
    curr_right_val = stuff[i][2]
    curr_direction = d
    right = i + 1
    while right < 4:
        next_left_val = stuff[right][6]
        # 같이 움질일 바퀴 확인
        if curr_right_val != next_left_val:
            to_move.append([right, -curr_direction])
            curr_right_val = stuff[right][2]
            curr_direction = -curr_direction
            right = right + 1
        else:
            break

    return to_move


def change(stuff, num, direction):
    temp = deque(stuff[num])
    temp.rotate(direction)
    return temp

def solution(stuff, orders):
    for n, d in orders:
        i = n-1
        to_move = check(stuff, i, d)
        for num, direction in to_move:
            stuff[num] = [i for i in change(stuff,num,direction)]

    result = 0
    for i, li in enumerate(stuff):
        if li[0]: result += 2**i

    return result


if __name__ == '__main__':
    A = [*map(int, list(sys.stdin.readline().strip()))]
    B = [*map(int, list(sys.stdin.readline().strip()))]
    C = [*map(int, list(sys.stdin.readline().strip()))]
    D = [*map(int, list(sys.stdin.readline().strip()))]
    K = int(input())
    inputs = [[*map(int,sys.stdin.readline().split())] for _ in range(K)]

    print(solution([A,B,C,D], inputs))