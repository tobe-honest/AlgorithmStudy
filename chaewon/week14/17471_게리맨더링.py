from collections import defaultdict, deque
from itertools import combinations
n=int(input()) 
population=[0]+list(map(int,input().split(' ')))
city=defaultdict(list)
global answer
answer=1e9
for i in range(n):
    seq=list(map(int,input().split(' ')))
    if len(seq[1:])>0:
        city[i+1]=seq[1:]

def bfs(team,city):
    visited=[False]*(len(population)+1)
    q=deque([team[0]])
    visited[team[0]]=True
    while q:
        now=q.popleft()

        for next in city[now]:
            if not visited[next]:
                if next in team:
                    q.append(next)
                    visited[next]=True
    return len(team)==sum(visited)

def count_population(red, blue):
    red_count, blue_count=0,0
    for r in red:
        red_count+=population[r]
    for b in blue:
        blue_count+=population[b]
    return abs(red_count-blue_count)

candidate=list()
for i in range(1,n):
    candidate.extend(list(combinations(city.keys(), i)))

if candidate:
    for blue in candidate:
        if bfs(blue,city):
            red=set(range(1,n+1))-set(blue)
            if bfs(list(red),city): 
                difference=count_population(red,blue)
                answer=min(difference, answer)
else:
    if len(population)-1==2:
        first_min=min(population[1:])
        population.remove(first_min)
        second_min=min(population[1:])
        answer=second_min-first_min
if answer==1e9:
    print(-1)
else:
    print(answer)