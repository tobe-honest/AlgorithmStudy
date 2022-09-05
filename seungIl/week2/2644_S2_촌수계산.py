# BaekJoon P2644 "촌수계산" (그래프 | S2)
"""
---[실수]---
부모 List 를 만든 후 쓸데없이 투포인터로 접근하려 함
애초에 총 개수(n)가 적기 때문에 2중 for 문으로도 가능
---[부족한 점]---
그래프 -> BFS/DFS 로만 생각하는 틀에서 벗어나는 게 필요
---[풀이]---
먼저 주어진 정보를 통해 각 자식들과 부모를 dictionary 로 묶어주고 (relationships)
두개의 타겟 모두 각각의 부모 List 를 생성 (find_parents())
그 후 그 List 에서 공통 값(공통 부모)가 있는 지 판단 후
해당 값의 idx 를 통해 주어진 조건으로 반환 (find_common_parents())
---[비고]---
메모리 : 30840 | 시간 : 68
전통적인 BFS/DFS 로 푼 친구의 풀이를 보고 싶음
"""


# find 부모 List
def find_parents(t, re):
    result = [t]
    ci = t  # 현재 위치
    while True:
        if ci not in re:
            break
        result.append(re[ci])
        ci = re[ci]

    return result


# 공통 부모 위치 찾기
def find_common_parents(t1s, t2s):
    for i in range(len(t1s)):
        for j in range(len(t2s)):
            if t1s[i] == t2s[j]:
                return i + j

    return -1


def solution(target, relation):
    t1, t2 = target

    relationships = {}  # 관계 생성 (key : 자식, val : 부모)
    for x, y in relation:
        relationships[y] = x

    t1_parents = find_parents(t1, relationships)  # find t1's 부모 List
    t2_parents = find_parents(t2, relationships)  # find t2's 부모 List
    return find_common_parents(t1_parents, t2_parents)  # find t1 and t2's common 부모


if __name__ == '__main__':
    n = int(input())
    target = list(map(int, input().split()))
    m = int(input())
    relation = [list(map(int, input().split())) for _ in range(m)]
    print(solution(target, relation))
