from itertools import combinations

def find():
    combi = list(combinations(chicken, M))
    length = set()
    
    for com in combi:
        total = 0
        for h_x, h_y in house: # 집 기준으로 거리 측정
            tmp = 1e9
            for x, y in com: # 치킨집과 거리 탐색
                if abs(h_x - x) + abs(h_y - y) < tmp:
                    tmp = abs(h_x - x) + abs(h_y - y)
            total += tmp
        length.add(total)

    print(min(length))

if __name__ == '__main__':
    N, M = map(int, input().split()) # 크기, 치킨집 수
    gmap = []
    chicken = []
    house = []
    for i in range(N):
        l = list(map(int, input().split()))
        for j in range(N):
            if l[j] == 2:
                chicken.append([i, j])
            if l[j] == 1:
                house.append([i, j])
        gmap.append(l)

    # 0 : 빈 칸, 1 : 집, 2 : 치킨집
    find()