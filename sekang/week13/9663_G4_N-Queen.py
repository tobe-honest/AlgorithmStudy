def Collocate(cnt):
    if cnt == n:
        global answer
        # print(graph)
        answer += 1
        return
    
    for i in range(n):
        if not visited[i]:
        
            graph[cnt] = i + 1

            flag = True
            for j in range(cnt):
                # 행은 다르기 때문에 열이 같거나 대각선이 같으면 배치 불가
                if abs(graph[cnt] - graph[j]) == abs(cnt - j) or graph[cnt] == graph[j]:
                    flag = False
                    break
            
            # 배치가 가능한 위치만 더 탐색
            if flag:
                # print(cnt, graph)
                visited[i] = 1
                Collocate(cnt + 1)
                visited[i] = 0
        

if __name__ == '__main__':
    n = int(input())
    visited = [0] * n
    graph = [0] * n
    answer = 0
    Collocate(0)

    print(answer)