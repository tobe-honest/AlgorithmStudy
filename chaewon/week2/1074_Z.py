import sys
n,target_r,target_c=map(int,sys.stdin.readline().split(' '))
size=2**n

graph=dict()
cnt=0 # 답이 될 포인터

# Z순서대로 : 왼위,오위,왼아래,오아래
dr=[0,0,1,1] 
dc=[0,1,0,1]

# 1,2,3,4 사분면(4등분했을 때)으로 나누었을 때 어디에 있는지 확인
def check_quad(r,c,now_r,now_c,size):
    rr=now_r+size//2
    cc=now_c+size//2
    if r<rr and c<cc: # 1사분면
        return 0
    elif r<rr and c>=cc: # 2사분면
        return 1
    elif r>=rr and c<cc: # 3사분면
        return 2
    elif r>=rr and c>=cc: # 4사분면
        return 3

def divide(r,c,size):
    global cnt
    if size==2: # 한 변의 길이가 2가 될 때만 graph에 그린다
        for i in range(4):
            graph[(r+dr[i],c+dc[i])]=cnt
            cnt+=1
    else:
        flag=check_quad(target_r,target_c,r,c,size) # 사분면 체크
        size//=2
        
        cnt+=size*size*flag # 진짜로 graph에 그리지 않고 cnt를 더해서 skip해줌

        plus=[[0,0],[0,size],[size,0],[size,size]] # 다음 분할을 위한 위치를 사분면에 따라 다르게 해줌
        divide(r+plus[flag][0], c+plus[flag][1], size)

divide(0,0, size)
print(graph[(target_r,target_c)])
