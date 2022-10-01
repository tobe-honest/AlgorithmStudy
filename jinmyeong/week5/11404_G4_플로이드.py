input = __import__("sys").stdin.readline

def floydwarshall(fw):
    dummy = [[fw[i][j] for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dummy[i][k] + dummy[k][j] < dummy[i][j]:
                    dummy[i][j] = dummy[i][k] + dummy[k][j]
                    
    dummy = [[0 if dummy[i][j] == INF else dummy[i][j] for j in range(N)] for i in range(N)]
    return dummy

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    INF = 999999999
    l = {i+1 : {j+1 : 0 if i==j else INF for j in range(N)} for i in range(N)}

    for _ in range(M):
        a, b, c = map(int, input().split())
        if l[a][b] > c:
            l[a][b] = c

    fw = [[l[k1][k2] for __, k2 in enumerate(l[k1])] for _, k1 in enumerate(l)]
    for idx, val in enumerate(floydwarshall(fw)):
        print(' '.join( list(map(str, (val)))))