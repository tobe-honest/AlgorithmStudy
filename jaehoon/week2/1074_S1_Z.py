def divide(x,y,size,type):
    if size==2:
        k=1
        for i in range(y,y+2):
            for j in range(x,x+2):
                    if r == i and c == j:
                        type.append(k)
                        break
                    k+=1
        return

    size = size // 2

    if x <= c < x+size and y <= r < y+size:
        type.append(1)
        divide(x,y,size,type)
    elif x+size <= c < x+size*2 and y <= r < y+size:
        type.append(2)
        divide(x+size,y,size,type)
    elif x <= c < x+size and y+size <= r < y+size*2:
        type.append(3)
        divide(x,y+size,size,type)
    elif x+size <= c < x+size*2 and y+size <= r < y+size*2:
        type.append(4)
        divide(x+size,y+size,size,type)


N,r,c = map(int,input().split())
type, result = [],0
divide(0,0,2**N,type)

for i in range(N):
    result = result + (type[i]-1)*(4**(N-i-1))
print(result)
