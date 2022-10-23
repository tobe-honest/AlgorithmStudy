from itertools import combinations

def find():
    combi = list(combinations(number, 6))

    for co in combi:
        for c in co:
            print(c, end=" ")
        print()
    print()


if __name__ == '__main__':
    while True:
        lotto = list(map(int, input().split()))
        if lotto == [0]:
            break
        k = lotto[0] # 6 < k < 13
        number = lotto[1:k+1]
        find()