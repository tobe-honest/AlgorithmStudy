def solve(depth):
    global result
    
    if depth == 11:
        result = max(result, sum(ans))
        return

    for i in range(11):
        if visited[i]:
            continue
        if val[depth][i]:
            visited[i] = 1
            ans.append(val[depth][i])
            solve(depth+1)
            ans.pop()
            visited[i] = 0

C = int(input())
for tc in range(C):
    val = [list(map(int, input().split())) for _ in range(11)]
    result,ans,visited = 0,[],[0]*11

    solve(0)
    print(result)