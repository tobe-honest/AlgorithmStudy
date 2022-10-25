import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        info = [0] + list(map(int, input().split()))
        visited = [0] * (n+1)
        group = 1
        for i in range(1, n+1):
            if visited[i] == 0:
                while visited[i] == 0:
                    visited[i] = group
                    i = info[i]
                while visited[i] == group:
                    visited[i] = -1
                    i = info[i]
                group += 1
            # print(visited)

        cnt = sum([1 for visit in visited if visit > 0])
        print(cnt)
