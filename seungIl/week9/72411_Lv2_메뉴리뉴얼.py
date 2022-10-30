# Programmers P72411 "메뉴 리뉴얼" (문자열, 자료구조, 정렬 | Lv2)
"""
---[실수]---
---[부족한 점]---
---[풀이]---
각 course의 값 만큼 조합을 구한 후
해당 조합을 count -> 동일한 조합일 경우 계속 똑같은 key에 count 되는 것
count의 결과를 정렬한 후
최대 개수와 동일한 모든 값을 저장
마지막으로 사전순으로 저장
---[비고]---
풀이 시간: 22m
"""
from collections import defaultdict
from itertools import combinations

# c값에 따른 info 생성 -> info : key=메뉴모음 튜플, val=개수
def make_info(c, orders):
    info = defaultdict(int)
    for order in orders:
        menu_li = list(sorted(order))
        for cased in combinations(menu_li, c):
            info[cased] += 1
    return info


def solution(orders, course):
    answer = []
    for c in course:
        # c값에 따른 info 생성 -> info : key=메뉴모음 튜플, val=개수
        info = make_info(c, orders)

        # c 가 문자열의 길이보다 긴경우 -> info에 한개도 만들어지지 않음 -> 조건 어김
        if len(info) == 0: continue

        # 결과 info를 count기준으로 정렬
        result_info = sorted(info.items(), key=lambda x: x[1], reverse=True)

        max_val = result_info[0][1]  # count 최대값
        if max_val < 2: continue  # 최대값이 2보다 작은 경우 -> 조건 어김

        # 최대값과 동일한 문자열 색출
        for menus, val in result_info:
            if val == max_val:
                answer.append(''.join(menus))
            else:
                break
    answer.sort()  # 사전 순으로 정렬
    return answer


if __name__ == '__main__':
    inputs1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    inputs2 = [2, 3, 4]
    print(solution(inputs1, inputs2))
