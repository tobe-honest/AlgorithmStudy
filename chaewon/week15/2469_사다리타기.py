k=int(input())
n=int(input())
final=input()

ladder=list()
for i in range(n):
    tmp=input().rstrip()
    ladder.append(tmp)
    if tmp[0]=='?':
        front=i # ? 전의 가로 줄 갯수        
back =n-1-front # ? 후의 가로 줄 갯수

# front 부분 이동 시키기
front_location=[0]*k
for i in range(k):
    location=i
    for j in range(front):
        if location<k-1 and ladder[j][location]=="-":
            location+=1
        elif location-1 >=0 and ladder[j][location-1]=="-":
            location-=1
    front_location[location]=chr(i+65)

# back 부분 이동 시키기
back_location=[0]*k
for i in range(k):
    location=i
    for j in range(1,back+1):
        if location<k-1 and ladder[-j][location]=="-":
            location+=1
        elif location-1 >=0 and ladder[-j][location-1]=="-":
            location-=1
    back_location[location]=final[i]
    
# front_location -> back_location
answer=['*']*(k-1)
cnt=0
for i in range(k):
    if front_location[i]==back_location[i]:
        cnt+=1
    elif i+1<k and front_location[i]==back_location[i+1]:
        cnt+=1
        answer[i]='-'
    elif 0<=i-1 and front_location[i]==back_location[i-1]:
        cnt+=1
        answer[i-1]='-'
if cnt==k:
    print(''.join(answer))
else:
    print('x'*(k-1))