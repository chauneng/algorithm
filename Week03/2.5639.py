import sys 

sys.setrecursionlimit(10 ** 7)
preorder = [] 

while True:
    try: 
        preorder.append(int(sys.stdin.readline())) 
    except: 
        break 

def preToPost(start, end):

    if end < start:
        return 

    node = preorder[start]
    div = (end + 1)

    for i in range(start+1, end+1):
        if node < preorder[i]:
            div = i
            break

    preToPost(start+1, div-1)
    preToPost(div, end)
    print(node)

preToPost(0, len(preorder)-1)