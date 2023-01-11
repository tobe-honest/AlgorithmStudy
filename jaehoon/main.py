n = int(input())
lst = list(map(int,input().split()))
lst_max = max(lst)
cum = 0
for val in lst:
    cum += val/lst_max * 100

print((cum/n))