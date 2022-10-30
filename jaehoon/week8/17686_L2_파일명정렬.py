import copy

def solution(files):
    answer,lst = [], []
    
    for id,file in enumerate(files):
        head,number,tail = [],[],[]
        
        for i in range(0,len(file)):
            if '0' <= file[i] <= '9':
                break
            elif not('0' <= file[i] <= '9'):
                head.append(file[i])
        
        for j in range(i,len(file)):
            if not('0' <= file[j] <= '9'):
                break
            elif '0' <= file[j] <= '9':
                number.append(file[j])
        
        for k in range(j,len(file)):
            tail.append(file[k])
            
        head = "".join(head).lower()
        number = int("".join(number))
        tail = "".join(tail)
        lst.append([head,number,tail,id])

    lst.sort(key = lambda x :(x[0], x[1]))
    
    for i in range(len(files)):
        answer.append(files[lst[i][3]])
        
    return answer