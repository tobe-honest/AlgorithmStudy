from itertools import combinations
l,c = map(int,input().split(' '))
seq= list(input().split(' '))
seq.sort()
answer=list()
candidates=list(combinations(seq,l))
for candidate in candidates:
    copy=list(candidate)
    flag_vowel,flag_consonant=False,False
    for alphbet in 'aeiou':
        if alphbet in candidate:
            copy.remove(alphbet)
            flag_vowel=True
    if len(copy)>=2:
        flag_consonant=True

    if flag_consonant and flag_vowel:
        answer.append(''.join(candidate))
    
for a in answer:
    print(a)