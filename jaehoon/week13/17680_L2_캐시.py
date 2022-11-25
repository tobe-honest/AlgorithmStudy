from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    recent = cities[0]
    if cacheSize == 0:
        answer = len(cities)*5
    else:
        for city in cities:
            if len(cache) < cacheSize:
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    answer += 1
                else:
                    cache.append(city)
                    answer += 5
                    
            elif len(cache) == cacheSize:
                if city in cache:
                    cache.remove(city)
                    cache.append(city)
                    answer += 1
                else:
                    cache.popleft()
                    cache.append(city)
                    answer += 5

    return answer