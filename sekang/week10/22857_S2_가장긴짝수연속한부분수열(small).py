import sys
input = sys.stdin.readline

def find():
    right = 0 # 우측 포인터
    cnt = 0 # 홀수의 개수
    ans = 0 # 가장 긴 연속 길이
    dist = 0 # 부분수열 길이
    flag = True # 인덱스 초과 확인용 변수

    for left in range(n): # 좌측 포인터
        while cnt <= k and flag: # 우측 포인터 이동 가능 여부 판단

            if s[right] % 2: # 홀수라면
                if cnt == k: # 최대 삭제
                    break
                cnt += 1 # 홀수에 k보다 작아야 늘어남
            dist += 1 # 항상 늘어남
            if right == n-1: # 인덱스 최대
                flag = False # while 안돌게
                continue
            right += 1 # 우측 포인터 이동

        ans = max(ans, dist-cnt) # 현재 수와 짝수의 수(= 전체 길이 - 홀수 개수) 비교

        if s[left] % 2: # 좌측 포인터가 for문으로 하나씩 이동하니까 현재 좌측 포인터에 홀수가 있으면 홀수 개수 -1
            cnt -= 1
        dist -= 1 # 길이가 줄어야 하니까 -1
    print(ans)
    return

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    find()