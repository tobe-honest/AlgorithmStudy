import heapq
import sys
n=int(sys.stdin.readline())
classes=[]
for _ in range(n):
    cn, start, end= map(int,sys.stdin.readline().split(' '))
    classes.append([start,end]) # 강의실 번호 필요 없음

classes.sort() # 시작시간이 이른것부터 정렬 # 끝 시간도 알아서 정렬 됨 -> 힙의 맨 첫번째 것만 비교해도 괜찮은 이유
room=[]
heapq.heappush(room,0)

for cl in classes:
    now=heapq.heappop(room)
    heapq.heappush(room,cl[1]) # 일단 무조건 강의는 해야되니까 넣고 # 여기가 강의실을 추가하는 곳
    if cl[0]<now: # heapq의 첫번째(=마지막 강의를 마친시간이 가장 이른 강의실)과 비교했을 때 보다도 강의 시작시간이 더 일찍이면 어쩔 수 없이 원래 있던 강의실은 둘 수밖에 없음
        heapq.heappush(room,now)
print(len(room))
