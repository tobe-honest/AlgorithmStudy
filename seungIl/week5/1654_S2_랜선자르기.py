# BaekJoon P1654 "랜선자르기" (이분 탐색 | S2)
"""
---[실수]---
모든 line을 사용해야 된다고 생각해서 end 를 min(lines)로 설정
-> 802, 743, 457, 539 가 있을 때, 각각의 line에서 적어도 하나는 챙겨야 된다 생각했던 것
-> 각각의 line을 모두 사용할 필요는 없음 -> 심지어 하나만 사용하는 경우도 있을 것
=> max(lines)
---[부족한 점]---
실전에서 해당 문제가 나왔을 때 이분 탐색이란 것을 바로 눈치챌 수 있을 지 의심됨
---[풀이]---
이분 탐색의 대상 : 자를 랜선 길이
이분 탐색의 대상 판단 조건 : 만들어진 개수
자를 랜선의 길이에 대해 이분탐색을 진행하며
해당 길이에 대해 랜선을 잘랐을 때의 결과 개수가 원하는 개수보다 크거나 같으면 -> 길이를 더 늘려서 잘랐을 때의 결과 개수를 줄일 수 있음
    => 최대 길이를 구해야 하므로 길이를 늘려가며 안될 때 까지 테스트 하는 것 => 최대 길이
해당 길이에 대해 랜선을 잘랐을 때의 결과 개수가 원하는 개수보다 작으면 -> 길이를 줄여서 잘랐을 때의 결과 개수를 늘려야 함
---[비고]---
풀이 시간 : 15m
메모리 : 30840 | 시간 : 96
"""
import sys


def cutting(length, lines):
    cnt = 0
    for line in lines:
        cnt += line//length
    return cnt

def solution(target,lines):
    s, e = 1, max(lines)
    result = 0
    while s <= e:
        mid = (s+e)//2
        cnt = cutting(mid,lines)
        if cnt >= target:
            s = mid + 1
            result = mid
        else:
            e = mid - 1

    return result



if __name__ == '__main__':
    K, N = map(int, input().split())
    inputs = [int(sys.stdin.readline().strip()) for _ in range(K)]
    print(solution(N,inputs))