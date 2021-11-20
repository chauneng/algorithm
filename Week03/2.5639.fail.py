import sys
sys.setrecursionlimit(10*9)

preorder = []

while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

def preToPost(start: int, end:int):
    if start > end:
        return
    else:
        div = 0
        node = preorder[start]
        for i in range(start+1, end+1):
            if node < preorder[i]:
                div = i
                break
        preToPost(start+1, div-1)
        preToPost(div, end)
        print(node)

preToPost(0, len(preorder)-1)
# for i in reversed(preorder):
#     print(i)