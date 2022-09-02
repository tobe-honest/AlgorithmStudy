n= int(input())
graph = []
for i in range(n):
    x=input()
    temp=list()
    for xx in x:
        temp.append(int(xx))
    graph.append(temp)

answer=''
def divide(x,y,length):
    global answer
    match=graph[x][y]
    is_matched=True
    for i in range(x,x+length):
        for j in range(y,y+length):
            if graph[i][j]!=match:
                is_matched=False
                break

    if is_matched:
        answer+=str(match)
    else:
        points=[]
        answer+='('
        points.append((x,y))
        points.append((x,y+length//2))
        points.append((x+length//2,y))
        points.append((x+length//2,y+length//2))
        
        for point in points:
            divide(point[0],point[1],length//2)
        answer+=')'

divide(0,0,n)
print(answer)
