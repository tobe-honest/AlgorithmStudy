def dfs(arr, v):
    if len(arr) == l: # 서로 다른 l개 뽑은 경우
        consonants = 0 # 자음 개수
        vowels = 0 # 모음 개수
        for a in arr:
            if a in 'aieou':
                vowels += 1
            else:
                consonants += 1
        if vowels >= 1 and consonants >= 2:
            print("".join(arr))
        return
    if v == c: # ch list에서 마지막에 도달한 경우
        return
    arr.append(ch[v])
    dfs(arr, v+1)
    arr.pop()
    dfs(arr, v+1)

if __name__ == '__main__':
    l, c = map(int, input().split())
    ch = sorted(input().split())

    dfs([], 0)