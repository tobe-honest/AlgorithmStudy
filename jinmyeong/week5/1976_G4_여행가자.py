input= __import__("sys").stdin.readline
def union(n1, n2, parent_num):
    a, b = find(n1, parent_num), find(n2, parent_num)
    if a > b: parent_num[a] = b  
    else: parent_num[b] = a
    return
def find(now, parent_num):
    if parent_num[now] != now:
        parent_num[now] = find(parent_num[now], parent_num)
    return parent_num[now]

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    l = [list(map(int, input().split())) for i in range(N)]
    path = list(map(int, input().split()))
    parent_num = [i for i in range(N)]
    no = False

    for i in range(N): 
        for j in range(N):
            if l[i][j]:
                union(i, j, parent_num)
    compare = parent_num[path[0]-1]
    for i in range(1, M):
        if compare != parent_num[path[i]-1]:
            no = True
            break
    print("NO") if no else print("YES")
