n=int(input())
seq=list(map(int,input().split(' ')))

dp_table=[0]*len(seq)

for i in range(len(seq)):
    dp_table[i]=max(seq[i],dp_table[i-1]+seq[i])
print(max(dp_table))
