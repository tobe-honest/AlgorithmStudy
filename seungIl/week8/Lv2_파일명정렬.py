# Programmers "파일명정렬" (구현, 문자열, 정렬 | LV.2)
"""
---[실수]---
isdigit() 함수 사용 못함
---[부족한 점]---
IDE 없는 상태에서 자주 사용하지 않던 함수를 잘 사용하지 못함
str.isdigit() or str.isnumeric()
---[풀이]---
먼저 . 으로 split 해서 tail 을 분리해줌
split 한 결과의 첫번쨰 값(head 와 num 이 있는 문자열)을
인덱스 하나 하나 돌면서 숫자면 그 이전까지를 head 로 설정해주고
인덱스가 끊어지는 지점까지를 num 으로 설정
그 후 해당 정보들을 info 에 key 를 index 로, value 를 [head, num] 으로 설정 후
value 에 대해서 sort
마지막으로 정렬된 결과의 index 값을 통해 원래의 str 을 가져옴
---[비고]---
풀이 시간 : 40m
"""

def solution(files):
    info = {}
    for idx, file in enumerate(files):
        split_file = file.split('.')
        head_num = split_file[0]
        head_num_li = list(head_num)

        # find head
        i = 0
        while i < len(head_num_li) and not head_num_li[i].isnumeric():
            i += 1
        head = ''.join(head_num_li[:i]).lower()

        # find num
        j = i
        while j < len(head_num_li) and head_num_li[j].isnumeric():
            j += 1
        num = int(''.join(head_num[i:j]))

        # key : index, value : [head, num]
        info[idx] = [head, num]

    # sort by [head, num]
        # 1. head
        # 2. num
    answer = []
    for key, _ in sorted(info.items(), key=lambda x: x[1]):
        answer.append(files[key])  # find original and append

    return answer


if __name__ == '__main__':
    inputs = []
    print(solution(inputs))
