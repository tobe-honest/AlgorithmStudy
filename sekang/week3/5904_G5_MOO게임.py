def recursive(n, k, cnt):
    if cnt >= n:
        # 3개 구간으로 나눠서 확인
        while True:
            if k == 0:
                print('m') if n - 1 == 0 else print('o')
                break
            # cnt 비교를 k가 증가하고 하므로 1을 빼주고 해야함
            left = (cnt - (k + 2)) // 2
            right = left + (k + 2)
            if 0 <= n < left:
                cnt = left
                k -= 1
            elif left <= n < right:
                print('m') if n - 1 == left else print('o')
                break
            else:
                cnt = left
                n -= right
                k -= 1
        return
    cnt = cnt * 2 + 1 + (k+2)
    recursive(n, k+1, cnt)

n = int(input())
recursive(n, 1, 3) # n, k, cnt