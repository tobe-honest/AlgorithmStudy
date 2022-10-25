def find():
    # 5x + 3y == N
    x = N // 5
    y = N // 3
    cnt = 0
    for i in range(x+1):
        if (N-5*i) % 3 == 0 and 0 <= (N-5*i) // 3 <= y:
            cnt = i + (N-5*i) // 3
        # print((N-5*i) % 3 == 0, (N-5*i) // 3)
    
    print(cnt) if cnt != 0 else print(-1)
    return

if __name__ == '__main__':
    # 3kg + 5kg 조합으로 적은 개수의 Nkg 만들기
    # -> 5kg을 기준으로 0~x까지 찾는게 적을 듯
    N = int(input())

    find()