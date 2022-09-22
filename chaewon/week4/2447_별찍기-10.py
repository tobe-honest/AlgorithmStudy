import sys
n=int(sys.stdin.readline())

def star(n):
    if n == 3 : #최소 단위
        return ['***','* *','***']

    else:
        x=star(n//3)
        empty=[' '*len(x) for _ in range(len(x))] # 가운데에 들어갈 빈 칸
        one_three=list()
        two=list()
        for i in range(len(x)):
            one_three.append(x[i]+x[i]+x[i]) # 첫 번째 구간 : 0 ~ n//3 행 과 세 번째 구간 : (n//3)*2 ~ 끝 행 이 같아서 재사용
            two.append(x[i]+empty[i]+x[i]) # 두 번째 구간 : n//3 행 ~ (n//3)*2행
        answer=one_three + two + one_three # 첫째 둘째 셋째 구간을 합침
        return answer
        

answer= star(n)
for _ in answer:
    print(_)
