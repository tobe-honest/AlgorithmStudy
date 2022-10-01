from collections import deque
input = __import__("sys").stdin.readline

def check(x, visited):
    return 0 <= x <= 100000 and not visited[x]
def search(start):
    visited = [False for i in range(100001)]
    q = deque([start])
    ans_cnt = 0
    answer = 999999999
    while q:
        x, cnt = q.popleft()
        visited[x] = True
        # 커지면 그 이상 봐도 의미 없음
        # 먼저 멈춰줘야 한 번 더 안돌아 감
        if cnt > answer:
            break
        # 같으면 answer = cnt
        # ans_cnt += 1
        # 어처피 최적으로 감
        if x == K:
            answer = cnt
            ans_cnt += 1
            continue
        
        if check(x+1, visited):
            q.append((x+1, cnt+1))
        if check(2*x, visited):
            q.append((2*x, cnt+1))
        if check(x-1, visited):
            q.append((x-1, cnt+1))
    return answer, ans_cnt


if __name__ == "__main__":
    N, K = map(int, input().split())
    print('\n'.join(list(map(str, search((N, 0))))))
