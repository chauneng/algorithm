from sys import stdin

n = int(stdin.readline())
tree = {}

for _ in range(n):
    key, left, right = stdin.readline().split()
    tree[key] = [left, right]

def preorder(key: str):

    print(key, end='')

    if tree[key][0] != '.':
        preorder(tree[key][0])

    if tree[key][1] != '.':
        preorder(tree[key][1])

def inorder(key: str):

    if tree[key][0] != '.':
        inorder(tree[key][0])

    print(key, end='')

    if tree[key][1] != '.':
        inorder(tree[key][1])

def postorder(key: str):

    if tree[key][0] != '.':
        postorder(tree[key][0])
    
    if tree[key][1] != '.':
        postorder(tree[key][1])

    print(key, end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')