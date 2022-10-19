
from itertools import combinations

def find(s, stack, l):
    # stack에 index를 넣어서 짝 위치 저장
    for idx in range(len(s)):
        if s[idx] == '(':
            stack.append(idx)
        elif s[idx] == ')':
            start = stack.pop()
            end = idx
            l.append([start, end])

    # 조합을 만들어서 1~l-1까지 고르는 조합을 만든다.
    for i in range(1, len(l)+1):
        combi = combinations(l, i)
        for j in combi:
            tmp = list(s)
            for start, end in j:
                tmp[start] = ''
                tmp[end] = ''
            answer.add(''.join(tmp))

if __name__ == '__main__':
    string = input()
    stack = []
    l = []
    answer = set()
    find(string, stack, l)
    
    for s in sorted(list(answer)):
        print(s)