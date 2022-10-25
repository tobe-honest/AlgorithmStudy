from collections import defaultdict,deque
# 입력
n,m=map(int,input().split(' ')) # n:사람의 수, m: 파티의 수
know=list(map(int,input().split(' ')))
party=list()
for i in range(m):
    x=list(map(int,input().split(' ')))
    party.append(x[1:])
# 빠르게 끝내기
if know[0]==0:
    print(m)
    exit()

know=set(know[1:])
valid=[1]*m # 파티의 가능 여부
participate=defaultdict(set)
valid_participate=[1]*(n+1) # 진실을 아는 사람 1, 모르는 사람 0

# {1:{1,3}, 2:{} } # 각 사람과 한 번이라도 겹친 것들 집합으로 추가
for i in range(m):
    for p in party[i]:
        participate[p].update(party[i])

for i in participate.keys(): # 자기 자신 집합에서 제거
    participate[i].remove(i)

# 누가 알고있는지 valid_particiate에 처리
for k in know:
    valid_participate[k]=0 # 알고있다고 처리
    q=deque([]+list(participate[k]))
    while q:
        now=q.popleft()
        
        if valid_participate[now]==0: # 이미 안다고 처리했으면 지나치기
            continue
        else:
            tmp=list(participate[now])
            if len(tmp)==1: # extend는 itertool이라 한 개만 들어있으면 에러남
                q.append(tmp[0])
            else:
                q.extend(tmp)
            valid_participate[now]=0
#valid_participate의 인덱스를 리스트화
final_know=[i for i in range(1,n+1) if valid_participate[i]==0]

for i in range(m):
    if valid[i]==0:
        continue
    for k in final_know:
        if k in party[i]:
            valid[i]=0
            break

print(sum(valid))