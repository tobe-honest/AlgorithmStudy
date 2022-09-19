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

# 처음 재귀 생각할 때, 그림판에서 작아지는 방향으로 접근하는 문제도 있지만
# 길이적으로 접근하는 문제도 존재
# 문자열도 len 함수 사용
# k가 1부터 시작했어야 함
# NoneType ??

# 리스트 전체에 같은 값 더하는거 없나?
# -> map or list comprehension ([list1[i] + list2[i] for i in range(len(list1))])

# 접근 1) 문자열 전부 만들어서 index 접근
# 접근 2) top-down 방식으로 접근
# 접근 3) m이 들어가는 인덱스만 list 만들어서 비교
# 여기까지 결론 : 문자열/리스트를 만들어서 접근하면 안되고 규칙을 찾아서 해야할 듯

# 접근 4) 길이를 기반으로 올라가다가 만족하는 부분부터 index로 분할정복으로 접근

# 변수 하나당 1바이트라 생각하면 범위가 1e9이므로 1기가로 생각 가능해서 변수를 저장해서 접근하는게 안된다고 생각이 가능함
