# https://school.programmers.co.kr/learn/courses/30/lessons/17686#
from collections import defaultdict
def solution(files):
    file_dict=defaultdict(list)
    for i, file in enumerate(files):
        file_dict[file]=['','',i,'']
        end_head=False
        end_number=False
        for f in file:
            if f.isnumeric() and end_number==False:
                end_head=True
                file_dict[file][1]+=f
            else:
                if not end_head:
                    file_dict[file][0]+=f
                else:
                    end_number=True
                    file_dict[file][3]+=f
    for file in files:
        file_dict[file][0]=file_dict[file][0].lower()
        file_dict[file][1]=int(file_dict[file][1])
        file_dict[file][3]=file_dict[file][3].strip()
    final=list(file_dict.values())
    final.sort(key=lambda x:(x[0],x[1],x[2]))
    answer=[]
    for f in final:
        answer.append(files[f[2]])
            
    return answer
