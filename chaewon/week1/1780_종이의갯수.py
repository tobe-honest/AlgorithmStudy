import sys
sys.setrecursionlimit(10**6)
n=int(input())
graph=list()
for _ in range(n):
    graph.append(list(map(int,input().split(' '))))
cnt_minusone, cnt_zero, cnt_one=0,0,0


def divide(x,y,length):
    global cnt_minusone, cnt_zero, cnt_one
    match=graph[x][y]
    is_matched=True
    for i in range(x,x+length):
        for j in range(y,y+length):
            if graph[i][j]!=match:
                is_matched=False
                break

    if is_matched:
        if match==-1:
            cnt_minusone+=1
        elif match==0:
            cnt_zero+=1
        elif match==1:
            cnt_one+=1 
    else:
        points=[]
        points.append((x,y))
        points.append((x,y+length//3))
        points.append((x,y+length//3*2))

        points.append((x+length//3,y))
        points.append((x+length//3,y+length//3))
        points.append((x+length//3,y+length//3*2))

        points.append((x+length//3*2,y))
        points.append((x+length//3*2,y+length//3))
        points.append((x+length//3*2,y+length//3*2))
        for point in points:
            divide(point[0],point[1],length//3)

divide(0,0,n)
print(cnt_minusone)
print(cnt_zero)
print(cnt_one)
