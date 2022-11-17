class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
    
def pre_order(node):
    print(node.data,end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data,end='')
    if node.right != None:
        in_order(tree[node.right])

def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data,end='')


N = int(input())
tree = {}
for _ in range(N):
    data,left,right = input().split()
    if left == '.': left = None
    if right == '.': right = None
    tree[data] = Node(data,left,right)

pre_order(tree['A']) # root -> left -> right
print()
in_order(tree['A']) # left -> root -> right
print()
post_order(tree['A']) # left -> right -> root