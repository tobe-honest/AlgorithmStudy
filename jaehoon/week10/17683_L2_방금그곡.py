def convert(s):
    s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return s

def solution(m, musicinfos):
    answer = []
    m = convert(m)
    
    for idx,info in enumerate(musicinfos):
        split_info = info.split(",")
        time = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])

        melody = ""
        temp = convert(split_info[3])
        for t in range(time):
            k = t % len(convert(temp))
            melody += temp[k]

        if m in melody:
            answer.append([time,idx,split_info[2]])
    
    if len(answer) == 0:
        return "(None)"
    else:
        answer.sort(key = lambda x :(-x[0], x[1]))
        return answer[0][2]