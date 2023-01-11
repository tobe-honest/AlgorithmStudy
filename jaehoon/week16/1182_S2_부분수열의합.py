l = ['a', 'b', 'c', 'd']
n = len(l)
r = 2
answer = []

def dfs(idx, list):
    if len(list) == r:
        answer.append(list[:])
        return

    for i in range(idx, n):
        dfs(i+1,list+[l[i]])

dfs(0, [])
print(answer)