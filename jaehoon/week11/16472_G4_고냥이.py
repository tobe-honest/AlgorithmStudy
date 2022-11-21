N = int(input())
text = input()

start,end = 0,1
arr = set([text[start]])
result = 0

while start < end:
    if end == len(text):
        result = max(result, end-start)
        break
    
    arr.add(text[end])
    
    if len(arr) == N:
        result = max(result, end-start+1)
        end += 1
    elif len(arr) > N:
        arr = set()
        start += 1
        arr.add(text[start])
        end = start + 1
    else:
        end += 1

print(result)