import sys
input = sys.stdin.readline

def search(relation, start, target, cnt):
    # 방문 처리
    visited[start] = True
    # target이 start의 관계 안에 있다면
    # [cnt+1, target찾았다] 반환
    if target in relation[start]:
        return [cnt+1, True]
    # start의 관계에서 dfs
    for r in relation[start]:
        if not visited[r]:
            visited[r] = True
            cnt_, is_find = search(relation, r, target, cnt+1)
            # target을 찾았다면 그대로 반환
            if is_find:
                return [cnt_, is_find]
    # 관계가 없다면
    # [아무값, target못찾았다] 반환
    return [cnt, 0]

if __name__ == "__main__":
    # 전체 사람 수
    N = int(input())
    # 촌수를 계산해야 하는 서로 다른 두 사람의 번호
    n1, n2 = map(int,input().split())
    # 부모 자식들 간의 관계 수
    M = int(input())
    # 관계 딕셔너리 초기화
    relation = {i : [] for i in range(1, N+1)}
    # 방문 여부 리스트 초기화
    visited = [False for j in range(N+1)]
    # 관계 딕셔너리 값 채우기 - 양방향
    for i in range(M):
        f, t = map(int, input().split())
        relation[f].append(t)
        relation[t].append(f)

    cnt, is_find = search(relation, n1, n2, 0)
    print(cnt) if is_find else print(-1)