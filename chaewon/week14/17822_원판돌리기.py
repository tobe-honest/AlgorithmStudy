n,m,t=map(int,input().split(' ')) # 원판의 수, 숫자 갯수, 돌리는 횟수

circle=list()
for _ in range(n):
    circle.append(list(map(int,input().split(' '))))

x,d,k=list(),list(),list()
for _ in range(t):
    xi,di,ki=map(int,input().split(' '))
    x.append(xi) # 배수
    d.append(di) # 0 시계, 1 반시계
    k.append(ki) # 칸수

def turn(circle, x,direction,k):
    for _ in range(k):
        for i in range(n):
            if (i+1)%x==0:
                if direction==0: # 시계
                    tmp=circle[i][-1]
                    for j in range(m-1, 0,-1):
                        circle[i][j]=circle[i][j-1]
                    circle[i][0]=tmp
                else:
                    tmp=circle[i][0]
                    for j in range(m-1):
                        circle[i][j]=circle[i][j+1]
                    circle[i][-1]=tmp

    return circle
def adjacent(circle):
    flag=True
    change_dict={-1:m-1,m:0}
    direction=[[1,0,-1,0],[0,1,0,-1]]
    new_circle=[c[:] for c in circle]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                dx,dy=i+direction[0][k],j+direction[1][k]
                dy=change_dict[dy] if dy==-1 or dy==m else dy
                if 0<=dx<n and 0<=dy<m:
                    if circle[i][j]!=0 and circle[dx][dy]==circle[i][j]:
                        new_circle[dx][dy]=0
                        new_circle[i][j]=0
                        flag=False
    if flag: # 인접한 수가 같은 것이 없을 때
        cnt, sum_circle=0,0
        for i in range(n):
            for j in range(m):
                if circle[i][j]!=0:
                    cnt+=1
                    sum_circle+=circle[i][j]
        if sum_circle<=0:
            mean_circle=0
        else:
            mean_circle=sum_circle/cnt
        for i in range(n):
            for j in range(m):
                if circle[i][j]==0:
                    continue
                if circle[i][j]<mean_circle:
                    circle[i][j]+=1
                elif circle[i][j]>mean_circle:
                    circle[i][j]-=1
        return circle

    return new_circle
for i in range(len(x)):
    circle=turn(circle,x[i],d[i],k[i])
    circle=adjacent(circle)
all_circle=sum(circle,[])
print(sum(all_circle))