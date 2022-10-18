def find():
    l.sort()
    left = 0
    right = N-1
    cnt = 0
    while left < right:
        if l[left] + l[right] > x: # index를 줄여야 함
            right -= 1
            continue
        elif l[left] + l[right] == x: # 오름차순 + 다른 양의 정수이므로 종료 가능
            cnt += 1
            left += 1
            right -= 1
        else: # l[left] + l[right] < x
            left += 1

    print(cnt)
    return

if __name__ == '__main__':
    N = int(input())
    l = list(map(int, input().split()))
    x = int(input())

    find()