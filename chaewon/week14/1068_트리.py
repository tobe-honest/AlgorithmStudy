from collections import defaultdict,deque
n=int(input())
nodes=list(map(int,input().split(' ')))
del_node=int(input())
tree=defaultdict(list)

for i,node in enumerate(nodes):
    tree[node].append(i)
    
if nodes[del_node]==-1 : # 들어오자 마자 루트이기 때문에 연산하지 않고 바로 끝
    print(0)
else:
    q=deque([del_node])
    all_node=set(range(-1,n)) # 루트노드=자식노드 가 되는 상황 때문에 -1 포함
    while q:
        del_node=q.popleft()    
        if del_node in tree.keys():
            for node in tree[del_node]:
                q.append(node)
            tree.pop(del_node) # 노드 자체를 트리에서 삭제
        
        # 해당 노드가 사라졌으니 자식 리스트에서도 삭제하여 관리
        for k in tree.keys():
            if del_node in tree[k]:
                tree[k].remove(del_node) 
                
        all_node.discard(del_node) # 전체 노드를 관리
        
    keys=list(tree.keys()) # 이렇게 하지 않으면 run time error -> tree.keys()가 중간에 삭제되는 에러
    for k in keys:
        if len(tree[k])==0:
            tree.pop(k) # 리프노드가 아닌 노드(부모노드)들만 key로 관리 하기 위해서
    print(len(all_node-set(tree.keys()))) # 남아있는 전체 노드 - 부모노드