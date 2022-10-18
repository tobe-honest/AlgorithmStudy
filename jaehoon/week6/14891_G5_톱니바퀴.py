def eval(gears):
    result= 0
    for i in range(4):
        if gears[i][0] == 1:
            result += 2**(i)
    return result

def rotate(gears,n,d):
    if d == 1: # 시계 방향으로 회전
        temp = gears[n][7]
        for j in range(7):
            gears[n][7-j] = gears[n][7-j-1]
        gears[n][0] = temp

    elif d == -1: # 반시계 방향으로 회전
        temp = gears[n][0]
        for j in range(7):
            gears[n][j] = gears[n][j+1]
        gears[n][7] = temp
    
    return gears

# N극은 0, S극은 1
def check(gears,n,d):
    left,right,direction = gears[n][6],gears[n][2], d

    dl = [0,0,0,0]
    dl[n] = d

    for i in range(n):
        if gears[n-1-i][2] == left:
            break
        else:
            direction = direction*-1
            dl[n-1-i] = direction
            left = gears[n-1-i][6]

    direction = d
    for i in range(n+1,4):
        if gears[i][6] == right:
            break
        else:
            direction = -direction
            dl[i] = direction
            right = gears[i][2]

    for i in range(4):
        gears = rotate(gears,i,dl[i])

    return gears

gears = []
for i in range(4):
    gears.append(list(map(int,input())))

#  1 시계방향, -1 반시계방향
k = int(input())
for i in range(k):
    n, d = map(int,input().split())
    gears = check(gears,n-1,d)

print(eval(gears))



