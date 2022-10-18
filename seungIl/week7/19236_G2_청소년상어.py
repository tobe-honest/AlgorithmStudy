# BaekJoon P19236 "청소년 상어" (구현, 시뮬레이션 | G2)
"""
---[실수]---
1.  while (0 <= sni < 4 and 0 <= snj < 4) and graph[sni][snj] != 0:
    로 설정해서 차근차근 search 하는데, 갈 수 없는 상황이 발생해 버리면 끝내버림
    => 갈 수 있는 모든 곳을 가보아야 하는데, 중간에 못가는 상황이 발생해버리면
        뒤에 더 갈 수 있는 위치에 대해서 search를 진행하지 않음
    => 즉, 못 가는 부분을 뛰어 넘어 갈 수 있는 모든 곳에 가는 것이 아니라 못가는 부분이 발생하면 멈춤
    =>   while step < 3:
            if (0 <= sni < 4 and 0 <= snj < 4) and graph[sni][snj] != 0:
                search 진행
            step += 1
        를 통해 못가는 부분은 건너 뛰고 갈 수 있는 모든 부분을 search
2.  빈 공간 처리를 안해줌.
    상어가 먹은 위치를 -1로 처리하고 다음으로 넘어갈 때는 빈공간 처리를 해줘야 하는데
    안해줌 -> 빈공간 0으로 처리
---[부족한 점]---
복잡한 구현에 대한 세부적으로 모두 생각하는 능력 부족
---[풀이]---
그래프에서의 물고기 번호, 해당 물고기의 방향을 따로 저장하여 관리
물고기들의 위치를 저장하는 dictionary 를 통해서 쉽게 1~16의 위치를 가져오도록 설정

dfs
1. 주어진 상어의 위치에서 시작
    a. 먼저 해당 위치에 대해 물고기 취식
        - 해당 위치에 상어가 존재하고 있다는 -1 표시
    b. 물고기 이동
        - 1~16 의 순서대로 물고기 이동 (먹힌 애들은 pass)
        - 주어진 방향으로 이동이 불가능한 경우 반시계로 돌리며 가능한지 확인
        - swap을 통해서 물고기 이동 구현
    c. 상어 이동 (핵심)
        - 현재 주어진 상어의 방향으로 갈 수 있는 모든 위치에 대해 또 다시 dfs 진행
            - 모든 위치 : 주어진 방향으로 한칸,두칸,세칸,네칸 이동 (step)
            - 이때 중요한 것은 graph 들을 복사해서 넣어줘야 다른 bfs 뿌리에 영향을 주지 않음
        - 갈 수 있는 방향을 한개라도 못 찾을 경우(check == False) 해당 결과값을 최대값과 비교
---[비고]---
풀이 시간 : 2h
메모리 : 30840 | 시간 : 72
"""


def dfs(curr, graph, dir_info, loc_info, d, eaten, result):
    # 상어의 물고기 취식
    sci, scj = curr  # 상어의 위치
    scd = dir_info[sci][scj]  # 상어의 방향

    before = graph[sci][scj]  # 상어가 먹을 물고기 번호
    eaten += before  # 상어가 먹은 누적 물고기

    graph[sci][scj] = -1  # 상어 위치 (상어:-1)
    dir_info[sci][scj] = -1  # 상어 위치
    loc_info[before] = [-1, -1]  # 먹힘 표시

    # 물고기 이동
    for i in range(1, 17):
        ci, cj = loc_info[i]
        if ci + cj == -2: continue  # 빈칸 or 먹힘
        # 가능한 방향으로 이동
        for k in range(8):
            next_d = (dir_info[ci][cj] + k) % 8
            di, dj = d[next_d]
            ni, nj = ci + di, cj + dj
            if (0 <= ni < 4 and 0 <= nj < 4) and graph[ni][nj] != -1:
                # 변경된 방향 정보 업데이트
                dir_info[ci][cj] = next_d

                # 물고기 번호 서로 변경 및 위치 정보 업데이트
                temp = graph[ni][nj]
                graph[ni][nj] = graph[ci][cj]
                loc_info[graph[ci][cj]] = [ni, nj]  # 실수
                graph[ci][cj] = temp
                loc_info[temp] = [ci, cj]  # 실수

                # 방향 정보 서로 변경
                temp = dir_info[ni][nj]
                dir_info[ni][nj] = dir_info[ci][cj]
                dir_info[ci][cj] = temp

                break

    # 상어 이동
    sdi, sdj = d[scd]
    sni, snj = sci + sdi, scj + sdj

    check = False
    step = 0
    while step < 3:
        if (0 <= sni < 4 and 0 <= snj < 4) and graph[sni][snj] != 0:
            check = True
            graph[sci][scj] = 0  # 빈칸 처리
            temp_graph = [[graph[i][j] for j in range(4)] for i in range(4)]
            temp_dir_info = [[dir_info[i][j] for j in range(4)] for i in range(4)]
            temp_loc_info = {k: v for k, v in loc_info.items()}
            dfs([sni, snj], temp_graph, temp_dir_info, temp_loc_info, d, eaten, result)
        sni, snj = sni + sdi, snj + sdj
        step += 1

    if not check:
        result[0] = max(result[0], eaten)


def solution(graph, dir_info):
    # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
    d = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

    loc_info = {}
    for i in range(4):
        for j in range(4):
            loc_info[graph[i][j]] = [i, j]

    result = [0]
    dfs([0, 0], graph, dir_info, loc_info, d, 0, result)
    return result[0]


if __name__ == '__main__':
    inputs = [[*map(int, input().split())] for _ in range(4)]
    inputs_graph = [[0, 0, 0, 0] for _ in range(4)] # 물고기 번호 그래프
    inputs_dir = [[0, 0, 0, 0] for _ in range(4)] # 물고기 방향 그래프
    for n in range(4):
        for m in range(8):
            if m % 2 == 0:
                inputs_graph[n][m // 2] = inputs[n][m]
            else:
                inputs_dir[n][m // 2] = inputs[n][m] - 1

    print(solution(inputs_graph, inputs_dir))
