n=int(input())

def find_moo(partition,k,n): # [10,15,25], 2, 11
    if k==0: # 가장 작은 단위일 때
        if n==1:
            return 'm'
        else:
            return 'o'

    if n<=partition[0]: # 1 구간
        # 다음 partition을 만들기 위한 작업
        k-=1
        k_len=nk[k]
        return find_moo([k_len,k_len+k+3,k_len*2+k+3],k,n) # [3,3+(1+3)=7,3+(1+3)+3=10] # 1구간이기 때문에 n을 조정하지 않아도 됌 
    elif partition[0]<n and n<=partition[1]: # 2 구간 == 중간
        n-=partition[0] # n 조정
        if n==1: # 맨 앞만 빼고 다 o이기 때문에
            return 'm'
        else :
            return 'o'
    elif partition[1]<n and n<=partition[2]: # 3 구간
        k-=1
        k_len=nk[k]
        return find_moo([k_len,k_len+k+3,k_len*2+k+3],k,n-partition[1]) # 3구간 이기 때문에 2구간 까지의 길이를 빼어 조정

nk=[0,3] # [0,3,10,25,56 ...] # s(k)의 길이를 저장 # nk[k+1]=len(s(k)) 
# nk 배열 자체가 원래 [3,10,25 ..] 와 같이 문제에서 주어진 k랑 인덱스가 맞으면 좋은데 nk[0]에 0이 있어야해서 k+1 인덱스에 길이 저장

k=0 # k가 몇까지 필요한지 구함
while True: # n이 굉장히 크기 때문에 모든 nk 배열을 만들기 보다 필요한 만큼만 만들기
    if nk[k]<n: 
        k+=1
        if k>=2: # k가 1일 때는 계산으로 넣을 수 없기 때문에 nk에서 미리 넣어줬었다. k=2부터는 앞의 수로 계산 가능
            nk.append(nk[k-1]*2+(k+2)) # 이미 위에서 k+1을 해줬으니까 k+3 대신 k+2   
    else:
        break
k-=1 # nk 배열 자체가 원래 [3,10,25 ..] 와 같이 문제에서 주어진 k랑 인덱스가 맞으면 좋은데 없어서 nk[0]에 0이 들어 있어서 k를 1 빼줌

k_len=nk[k] # 10 # s(k)의 전체 길이
partition=[k_len,k_len+k+3,k_len*2+k+3] # [10 15 25] # s(k-1)의 끝 index , 앞 index + 추가된 moo 의 끝 index, 앞 index + s(k-1)의 끝 index# ([10 15 25],2,11)
print(find_moo(partition,k,n))
