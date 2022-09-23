from collections import deque
import sys
input=sys.stdin.readline

# 현재 좌표로 부터 타겟으로하는 좌표까지의 거리가 1000이하인지 판별
def check(nx, ny, target_x, target_y):
    return True if abs(nx - target_x) + abs(ny - target_y) <= 1000 else False

def search(start, cs):
    q = deque([start])
    # (1000, 1000) : False 이런 형태로 초기화
    visited = {cs[i]:False for i in range(N)} 
    # bfs
    while q:
        nx, ny = q.popleft()
        # 현재 좌표 ~ 페스티벌 좌표 거리가 1000이하이면 True
        if check(nx, ny, fest_x, fest_y):
            return True
        
        # 현재 좌표 ~ 페스티벌 좌표 거리가 1000이하가 아니면
        # 편의점 들리면서 갈 수 있는지 확인
        for i in range(N):
            # 방문하지 않은 편의점이라면,
            # 방문처리 하는 것이 없으면 중구난방으로 다님;
            cx, cy = cs[i]
            if not visited[cs[i]] and check(nx, ny, cx, cy):
                    visited[(cx, cy)] = True
                    q.append((cx, cy))
            # 현재 좌표 ~ 방문하지 않은 편의점 좌표 거리가 1000이하이면
            # 방문처리 + queue에 추가
            # bfs로 같은 레벨의 좌표를 모두 방문처리 해도 됨
            # why? => 어차피 못가는 곳은 여기서 걸러짐

    return False

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        home_x, home_y = map(int, input().split())
        cs = [tuple(map(int, input().split())) for i in range(N)]
        fest_x, fest_y = map(int, input().split())
        now_x, now_y = home_x, home_y
        if search((home_x, home_y), cs):
            print("happy")
        else:
            print("sad")
        