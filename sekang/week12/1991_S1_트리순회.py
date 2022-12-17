class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node): # 전위 순회 (루트-왼-오)
    print(node.data, end='')
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

def in_order(node): # 중위 순회 (왼-루트-오)
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != None:
        in_order(tree[node.right])

def post_order(node): # 후위 순회 (왼-오-루트)
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end='')

if __name__ == '__main__':
    n = int(input())
    tree = {}
    for _ in range(n):
        data, left, right = input().split()
        if left == '.':
            left = None
        if right == '.':
            right = None
        tree[data] = Node(data, left, right)
    
    # print(tree['A'].left)
    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])