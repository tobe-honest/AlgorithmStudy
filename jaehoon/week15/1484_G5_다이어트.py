if __name__== '__main__':
    G = int(input())
    now = [x for x in range(1, 100001)]
    remember = [x for x in range(1, 100001)]
    left, right = 0, 0
    result = []
    while left < 100000 and right < 100000:
        temp = (now[left])**2 - (remember[right])**2
        if temp == G: result.append(now[left])
        if temp < G:
            left += 1
        else:
            right += 1

    if len(result) == 0:
        print(-1)
    else:
        for val in result:
             print(val)