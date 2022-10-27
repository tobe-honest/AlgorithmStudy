from itertools import combinations

def comb(lst,num):
	ans = []
	if num > len(lst): return ans # 빈 값 반환

	if num == 1: # num 1이면 그냥 lst 하나씩 담기
		for i in lst:
			ans.append([i])
	elif num>1:
		for i in range(len(lst)):
			for temp in comb(lst[i+1:],num-1):
				ans.append([lst[i]]+temp)

	return ans

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break
    else:
        lst.remove(lst[0])

    can = list(comb(lst,6)) # 함수로 직접 짜보기
    can.sort()
    for i in range(len(can)):
        for j in range(len(can[i])):
            print(can[i][j], end=" ")
        print("",end="\n")
    print("",end="\n")