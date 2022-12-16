n,m,x,y,k=map(int, input().split(' '))
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split(' '))))
command=list(map(int, input().split(' ')))

dice=[0,0,0,0,0,0] # 밑, 동, 서, 남, 북, 위

def north(dice):
    new_dice=[0,0,0,0,0,0]
    new_dice[0]=dice[4]
    new_dice[1]=dice[1]
    new_dice[2]=dice[2]
    new_dice[3]=dice[0]
    new_dice[4]=dice[5]
    new_dice[5]=dice[3]
    return new_dice

def south(dice):
    new_dice=[0,0,0,0,0,0]
    new_dice[0]=dice[3]
    new_dice[1]=dice[1]
    new_dice[2]=dice[2]
    new_dice[3]=dice[5]
    new_dice[4]=dice[0]
    new_dice[5]=dice[4]
    return new_dice

def west(dice):
    new_dice=[0,0,0,0,0,0]
    new_dice[0]=dice[2]
    new_dice[1]=dice[0]
    new_dice[2]=dice[5]
    new_dice[3]=dice[3]
    new_dice[4]=dice[4]
    new_dice[5]=dice[1]
    return new_dice

def east(dice):
    new_dice=[0,0,0,0,0,0]
    new_dice[0]=dice[1]
    new_dice[1]=dice[5]
    new_dice[2]=dice[0]
    new_dice[3]=dice[3]
    new_dice[4]=dice[4]
    new_dice[5]=dice[2]
    return new_dice

for c in command:
    flag=True
    if c ==1 : # 동
        dy=y+1
        if 0<=dy<m:
            dice=east(dice)
            y=dy
        else:
            flag=False
    elif c==2:
        dy=y-1
        if 0<=dy<m:
            dice=west(dice)
            y=dy
        else:
            flag=False
    elif c==3:
        dx=x-1
        if 0<=dx<n:
            dice=north(dice)
            x=dx
        else:
            flag=False
    elif c==4:
        dx=x+1
        if 0<=dx<n:
            dice=south(dice)
            x=dx
        else:
            flag=False
    if flag:
        if graph[x][y]==0:
            graph[x][y]=dice[0]
        else:
            dice[0]=graph[x][y]
            graph[x][y]=0

        print(dice[5])