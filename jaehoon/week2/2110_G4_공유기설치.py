import sys
def give_me_solution(min_distane, max_distance):
    while min_distane <= max_distance:
        distance = (min_distane+max_distance) // 2
        point,count = 0,1
        for i in range(N):
            if abs(house[i] - house[point]) >= distance:
                count += 1
                point = i
        if count < C:
            max_distance = distance-1
        else:
            min_distane = distance+1

    return (min_distane+max_distance)//2


N,C = map(int,input().split())
house= []
for i in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()
answer = give_me_solution(1, abs(house[-1] - house[0]))
print(answer)