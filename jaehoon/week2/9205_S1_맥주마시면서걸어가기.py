
def check(startx,starty,targetx,targety):
    distance = abs(targetx - startx) + abs(targety - starty)
    if distance <= 1000:
        return True
    else:
        return False

def search(x,y):
    global flag

    if check(x,y,goalx,goaly):
        flag=1
        return

    for i in range(n):
        if check(x,y,martx[i],marty[i]) and visited[i] == False:
            visited[i]=True
            search(martx[i],marty[i])

t = int(input())
for i in range(t):
    martx, marty = [], []
    n = int(input())
    homex,homey = map(int,input().split())
    for j in range(n):
        tempx,tempy = map(int,input().split())
        martx.append(tempx)
        marty.append(tempy)
    goalx,goaly = map(int,input().split())
    flag=0
    visited = [False for i in range(n)]
    search(homex,homey)
    if flag==0:
        print("sad")
    else:
        print("happy")
    
