def solve(depth,v):
    global result
    
    if depth == n:
        if len(set(path)) == n:
            result = min(result,sum(ans))
        return

    for i in range(n):
        if visited[i]:
            continue
        
        if board[v][i] != 0:
            visited[i] = 1
            ans.append(board[v][i])
            path.append(v)
            solve(depth+1,i)
            ans.pop()
            path.pop()
            visited[i] = 0

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

result,ans,visited,path = 1e9,[],[0]*n,[]
solve(0,0)
print(result)