from collections import defaultdict
n=int(input())
graph=defaultdict()

for i in range(n):
    d,l,r= input().split(' ')
    l= None if l == '.' else l
    r= None if r == '.' else r
    graph[d]=[l,r]

def preorder(now):
    left,right=graph[now]
    print(now,end='')
    if left !=None:
        preorder(left)
    if right !=None:
        preorder(right)

def inorder(now):
    left,right=graph[now]
    
    if left !=None:
        inorder(left)
    print(now,end='')
    if right !=None:
        inorder (right)

def postorder(now):
    left,right=graph[now]
    
    if left !=None:
        postorder(left)
    if right !=None:
        postorder(right)
    print(now,end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')