# 번역기 : 문자열에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열만 인식 가능
# 입력 : 문자열
# 출력 : 번역기가 인식할 수 있는 최대 문자열의 길이

n = int(input())    
string = input()
cnt = 0
answer = 0
i = j = 0
S = set()

while j < len(string):
    
    if string[j] not in S:
        if len(S) == n: # count 불가
            S.clear()
            cnt = 0
            i += 1
            j = i
        else:
            S.add(string[j])
            j += 1
            cnt += 1
            answer = max(answer, cnt)
    else:
        j += 1
        cnt += 1
        answer = max(answer, cnt)
    
print(answer)