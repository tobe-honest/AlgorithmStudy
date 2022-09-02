# BaekJoon P7795 "먹을 것인가 먹힐 것인가" ( 이진탐색, 투포인터| S3)
"""
<유형: 이진탐색(+투 포인터)>
---[실수]---
처음에 2중 for문으로 전수조사로 하려함 -> 최대 20,000 의 요소를 2중 반복하면 당연히 시간 초과
---[부족한 점]---
이진탐색에 대해 많이 풀어보지 못했음
---[풀이]---
이진탐색(+투 포인터)로 풀이 진행
각 B에 해당하는 원소들이 A로 들어갔을 때의 위치를 알아낸 후
해당 B의 원소의 위치 전의 모든 A의 원소를 조건에 맞는 원소라 생각하고 Count!
---[비고]---
Basic 이진탐색(while s <= e)과는 다른 이진탐색(while s < e)
Basic 이진탐색 => 타겟이 주어지고 해당 타겟의 리스트 속 위치를 알아내는 것 -> 즉, 원하는 타겟이 리스트안에 있으면 해당 위치를 반환 아니면 None 반환 등
해당 문제에서의 이진 탐색 => 타겟이 주어지고 해당 타겟의 리스트 속 위치를 알아내는데,
                        리스트 속 타겟의 값을 가지는 요소의 위치를 알아내는 것이 아닌, 타겟의 값의 크기에 따라 위치를 찾는 것
- 이진탐색 의외의 알고리즘으로도 풀 수 있는지 논의하고 싶음
"""
import sys


def solution(a, b):
    answer = 0
    for i in b:
        s, e = 0, len(a) - 1
        while s < e:  # while s<=e 시 오류 => s와 e가 동일한 경우 while 문을 종료해주어야 함
            m = (s + e) // 2
            if i < a[m]:
                s = m + 1
            else:
                e = m - 1

        final_idx = s

        if i < a[s]:
            answer += final_idx + 1
        else:
            answer += final_idx

    return answer


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, M = map(int, sys.stdin.readline().split())
        arr1 = list(map(int, sys.stdin.readline().split()))
        arr2 = list(map(int, sys.stdin.readline().split()))
        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        print(arr1, arr2)
        print(solution(arr1, arr2))
