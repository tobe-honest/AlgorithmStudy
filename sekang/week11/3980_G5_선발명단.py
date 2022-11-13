def permutation(player, score):
    global max_score
    if player == 11:
        max_score = max(max_score, score)
        return

    for i in range(11):
        if visited[i] or not info[player][i]: # 이미 자리 선점 or 부적합(0점)
            continue
        visited[i] = True
        permutation(player + 1, score + info[player][i])
        visited[i] = False

t = int(input())
for _ in range(t):
    info = [list(map(int, input().split())) for _ in range(11)]
    max_score = 0
    visited = [False] * 11
    permutation(0, 0)
    print(max_score)