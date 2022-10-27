# BaekJoon P2800 "괄호제거" (자료구조, 스택 | G5)
"""
---[실수]---
1. "어떤 식을 여러 쌍의 괄호가 감쌀 수 있다." -> ((1))과 같은 경우를 무시함
    => 결과들을 저장하는 공간을 list 가 아닌 set 으로 설정 -> 중복 제거
---[부족한 점]---
---[풀이]---
먼저 괄호쌍의 인덱스 정보를 스택을 통해 찾아 준 후 각 괄호쌍의 인덱스 정보를 저장 -> info = ex) [[1,4],[0,6]]
총 info 의 개수까지 combinations(조합) 진행 -> step => ex) info len = 4 / step = 1,2,3,4
step 은 제거할 괄호쌍의 개수
step 을 통해서 해당 개수에 맞게 괄호쌍 제거 -> 조합 사용
---[비고]---
풀이 시간 : 22m
메모리: 32436 | 시간: 88
재귀로 푼 사람이 있는지 궁금
"""
from collections import deque
from itertools import combinations


def solution(operation):
    info = []
    stk = deque([])
    # 괄호쌍 찾기
    for idx, c in enumerate(operation):
        if c == '(':
            stk.append(idx)
        elif c == ')':
            info.append([stk.pop(), idx])

    # 조합에 따른 괄호 제거
    answer = set()
    for step in range(1,len(info)+1):
        for choiced in combinations(info,step):
            temp = list(operation)
            for first, end in choiced:
                temp[first] = temp[end] = ''
            answer.add(''.join(temp))

    return sorted(answer)

if __name__ == '__main__':
    inputs = input()
    print(*solution(inputs), sep='\n')