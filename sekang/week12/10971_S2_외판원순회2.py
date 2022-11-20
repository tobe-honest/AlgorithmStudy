def TSP(visited, k, score, cnt, start):
    
    if cnt == n:
        # print(score)
        if W[k][start]:
            global answer
            answer = min(answer, score + W[k][start])
        return
    
    if score > answer:
        return

    for i in range(n):
        if not visited[i] and W[k][i]:
            visited[i] = 1
            TSP(visited, i, score + W[k][i], cnt + 1, start)
            visited[i] = 0

if __name__ == '__main__':
    n = int(input())
    W = [list(map(int, input().split())) for _ in range(n)]
    answer = 1e9
    visited = [0] * n
    
    for k in range(n):
        visited[k] = 1
        TSP(visited, k, 0, 1, k)
        visited[k] = 0

    print(answer)