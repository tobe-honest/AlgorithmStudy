n= int(input())
graph = []
for i in range(n):
    x=input()
    temp=list()
    for xx in x:
        temp.append(int(xx))
    graph.append(temp)

def dfs(x, y,n_house):

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False,n_house

    if graph[x][y] == 1:
        n_house+=1
        graph[x][y] = 0 # 방문 처리
        _,n_house=dfs(x - 1, y,n_house)
        _,n_house=dfs(x, y - 1,n_house)
        _,n_house=dfs(x + 1, y,n_house)
        _,n_house=dfs(x, y + 1,n_house)
        
        return True,n_house
    return False,n_house

result = 0
houses=list()
for i in range(n):
    for j in range(n):
        is_danji,n_house=dfs(i, j,0)
        if is_danji == True:
            result += 1
            houses.append(n_house)
            

print(result)
houses.sort()
for house in houses:
    print(house)
