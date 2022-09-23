def binary_search(target, lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    if end>=start:
        return end
    else:
        return end+1
    

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    lsta,lstb,count = [],[],0
    lsta = (list(map(int,input().split())))
    lstb = (list(map(int,input().split())))
    lsta.sort()
    lstb.sort()

    for i in range(len(lsta)):
        count = count + binary_search(lsta[i],lstb)
    print(count)


    

        