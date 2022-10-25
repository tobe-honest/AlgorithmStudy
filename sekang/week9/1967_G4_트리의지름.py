import sys
sys.setrecursionlimit(10000)

def dfs(x, prev_cost):
    for a, curr_cost in graph[x]:
        if visited[a] == -1: # 방문 안한 경우만 탐색
            visited[a] = prev_cost + curr_cost
            dfs(a, prev_cost + curr_cost)

if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    # step1) 시작 노드 1에서 가장 먼 노드 찾기
    visited = [-1] * (n + 1)
    visited[1] = 0 # 시작 노드 비용 초기화
    dfs(1, 0) # 노드1부터 각 노드까지 가는 비용 탐색

    # print(visited[1:]) # 비용 확인

    # step2) 시작 노드 1에서 가장 먼 노드에서 다시 가장 먼 노드 찾기
    far_node = visited.index(max(visited))

    visited = [-1] * (n + 1)
    visited[far_node] = 0  # 시작 노드 비용 초기화
    dfs(far_node, 0)

    # print(visited[1:])
    print(max(visited))