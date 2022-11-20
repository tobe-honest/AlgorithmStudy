def turn_key(key): # 시계 방향으로 90도씩 돌리기
    # 왼쪽 아래에서부터 위로 올라가게끔 원래 key를 읽으면 됨
    new_key=[[0]*len(key) for _ in range(len(key))]
    for nk_i,k_ii in zip(range(len(key)), range(len(key))): # nk:원래 for문 돌리듯이 그대로 넣어줌 # k:열은 그대로 읽기(왼->오)
        for nk_j,k_jj in zip(range(len(key)),range(len(key)-1,-1,-1)): # k:왼쪽 밑에서부터(밑->위)
            new_key[nk_i][nk_j]=key[k_jj][k_ii]
    return new_key

def solution(key, lock):
    answer = False
    n,m=len(lock),len(key)
    
    new_keys=list() # 키 4개가 담김
    new_keys.append(key)
    for i in range(3):
        key=turn_key(key)
        new_keys.append(key[:])
    
    # lock 확장 (zero-padding = m-1)
    for i in range(len(lock)):
        lock[i]=[0]*(m-1) + lock[i] + [0]*(m-1)
    add_list=[[0]*(2*(m-1) + n) for _ in range(m-1)]
    lock=add_list+lock+add_list

    for p in range(4): # key 별로
        now_key=new_keys[p]
        for i in range(n+m-1): # 전체 lock의 row
            for j in range(n+m-1): # 전체 lock의 column
                # key로 돌림
                flag=True # 해당 키의 가능 여부
                cnt=0
                
                # tmp_lock 생성
                tmp_lock=[llock[:] for llock in lock]
                for k in range(m):
                    for l in range(m):
                        tmp_lock[i+k][j+l]+=now_key[k][l]
                        
                # padding을 제외한 원래 lock 칸들에만 대해서 1인지 모두 확인
                for w in range(m-1,n+m-1): 
                    for h in range(m-1,n+m-1):
                        if tmp_lock[w][h]!=1:
                            flag=False
                            break
                    if flag==False: # 2중 for 문을 빠르게 빠져나오기 위해
                        break
                if flag==True: # 이번 key가 정답이면 이제 정답을 찾았으니 전체 for문을 빠져나오기
                    answer=True
                    break
                    
            if answer:
                break
        if answer:
            break
    return answer