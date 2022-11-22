def solve(depth):
    global result
    
    if depth == m:
        for i in range(m):
            print(ans[i],end=" ")
        print("")
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        ans.append(i+1)
        solve(depth+1)
        ans.pop()
        visited[i] = 0

n,m = map(int,input().split())
result,ans,visited = 0,[],[0]*n
solve(0)