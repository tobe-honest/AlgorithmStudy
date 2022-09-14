def recursive(a, b):
    if b == 1:
        return a
    elif b == 2:
        return a**2
    else:
        if b % 2: # 홀수
            return recursive(a, (b // 2))**2 * a
        else: # 짝수
            return recursive(a, (b // 2))**2

a, b, c = map(int, input().split())

print(pow(a,b,c))

# print(recursive(a, b) % c)