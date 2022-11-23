n=int(input())
seq=list(map(int,input().split(' ')))
start=0
end=n-1

candidate=list()
while start<end:
    value=seq[start]+seq[end]
    candidate.append([abs(value),seq[start],seq[end]])
    if value==0:
        break
    elif value>0:
        end-=1
    else:
        start+=1
candidate.sort()
print(candidate[0][1],candidate[0][2])