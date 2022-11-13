# Programmers P17683 "방금그곡" (문자열, 정렬 | Lv2)
"""
---[실수]---
temp가 matching에 없는 경우가 있었음
---[부족한 점]---
천천히 생각하고 천천히 풀자..
몇번의 시도 끝에 성공 -> 실전에선 그냥 틀린 문제다.
---[풀이]---
먼저 #에 해당하는 음표들을 custom 하게 바꿔주고
시간에 따라 해당 곡을 한줄의 음표로 구성된 음악으로 표현한 뒤
그 한줄의 음표로 구성된 음악 에 내가 들은 음악이 포함되어 있는지 판단
이후 길이 및 나온 순서로 정렬하여 반환
---[비고]---
풀이시간: 50m??
"""
def make_real(song):
    matching = {'A#': '1', 'C#': '2', 'D#': '3', 'F#': '4', 'G#': '5'}
    real = []
    i = 0
    while i < len(song):
        if i + 1 < len(song) and song[i + 1] == '#':
            temp = song[i] + song[i + 1]
            if temp in matching:
                real.append(matching[temp])
            i += 2
        else:
            real.append(song[i])
            i += 1

    return real


def solution(m, musicinfos):
    real_m = make_real(list(m))
    m_str = ''.join(real_m)

    answer = []
    for idx, info in enumerate(musicinfos):
        start, end, title, song = info.split(',')
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        s = 60 * sh + sm
        e = 60 * eh + em
        length = e - s
        real_song = make_real(song)
        heard = []
        for i in range(length):
            i = i % len(real_song)
            heard.append(real_song[i])
        heard_str = ''.join(heard)
        if m_str in heard_str:
            answer.append([length, -idx, title])

    if len(answer) == 0:
        return '(None)'
    else:
        return sorted(answer, reverse=True)[0][2]

if __name__ == '__main__':
    m = "ABCDEFG"
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    print(solution(m, musicinfos))