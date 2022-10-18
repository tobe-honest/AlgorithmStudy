import sys
input=sys.stdin.readline

wheel=list()
for i in range(4):
    tmp=input().rstrip()
    wheel.append([])
    for t in tmp:
        wheel[i].append(int(t))
# N극은 0, S극은 1

k = int(input()) #회전 횟수
opposite_direction={1:-1,-1:1}

def turn(turn,wheel):
    for num, dir in turn:
        if dir == 1: # 시계
            last = wheel[num][7]
            for i in range(6,-1,-1):
                wheel[num][i+1]=wheel[num][i]
            wheel[num][0]=last
        elif dir == -1 : # 반시계
            first=wheel[num][0]
            for i in range(1,8):
                wheel[num][i-1]=wheel[num][i]
            wheel[num][7]=first
    return wheel

for _ in range(k):
    num, ori_direction=map(int, input().split(' ')) #di=1->시계, -1 -> 반시계
    num-=1 # 돌아가는 톱니바퀴 번호 (인덱스라 1 빼줌)

    left,right=num-1,num+1
    r_turnable, l_turnable=True,True
    have_to_turn=list()
    have_to_turn.append([num, ori_direction])
    now=num
    direction=ori_direction
    while left>=0 and l_turnable: # 왼쪽으로 전파
        if wheel[now][6]!=wheel[left][2]:
            have_to_turn.append([left, opposite_direction[direction]])
            now=left
            left-=1
            direction=opposite_direction[direction]
        else:
            l_turnable=False # 이제 전파 불가

    now=num
    direction=ori_direction
    while right<4 and r_turnable: # 오른쪽으로 전파
        if wheel[now][2] != wheel[right][6]:
            have_to_turn.append([right, opposite_direction[direction]])
            now=right
            right+=1
            direction=opposite_direction[direction]
        else:
            r_turnable=False
    wheel=turn(have_to_turn,wheel)

answer=0
score=1
for i in range(4):
    if wheel[i][0]==1:
        answer+=score
    score*=2
print(answer)
