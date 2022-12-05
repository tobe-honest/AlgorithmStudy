from collections import deque
def solution(cacheSize, cities):
    answer = 0
    box=list()
    if cacheSize==0:
        return len(cities)*5
    for city in cities:
        city=city.lower()
        if city in box:
            answer+=1
            box.remove(city)
            box.append(city)
        else:
            answer+=5
            if len(box)==cacheSize:
                box=box[1:]
                box.append(city)
            elif len(box)<cacheSize:
                box.append(city)
                
    return answer