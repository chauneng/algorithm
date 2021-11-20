import sys
import math

sys.setrecursionlimit(10**6)

#세그먼트 트리 만드는 과정
def mTree(li, tree, node, start, end): 
    if start == end:
        tree[node-1] = start
    else:
        mid = (start+end)//2
        mTree(li, tree, node*2, start, mid)
        mTree(li, tree, node*2+1, mid+1, end)

        if li[tree[node*2-1]] < li[tree[node*2]]:
            tree[node-1] = tree[node*2-1]
        else:
            tree[node-1] = tree[node*2]

#구간내 최솟값을 찾아주는 쿼리함수
def query(li, tree, node, start, end, x, y):
    if x > end or y < start:
        return -1
    if start >= x and end <= y:
        return tree[node-1] 

    mid = (start+end)//2
    left = query(li, tree, node*2, start, mid, x, y)
    right = query(li, tree, node*2+1, mid+1, end, x, y)

    if left == -1:
        return right
    if right == -1:
        return left

def dac(start, end):
    index= query(li, tree, 1, 0, len(li)-1, start, end)

    if abs(end-start)==0:
        return li[index]
    
    v1, v2, v3 = li[index] * (end-start+1), 0, 0

    if index-1 >= start:
        v2 = dac(start, index-1)
    if index+1 <= end:
        v3 = dac(index+1, end) 

    return max(v1, v2, v3)

while(True):

    num = list(map(int, sys.stdin.readline().split()))
    if num[0]==0:
        break

    li = num[1:]
    tree =[0] * (pow(2, math.ceil(math.log(len(li), 2))+1)-1)

    mTree(li, tree, 1, 0, len(li)-1)
    print(dac(0, len(li)-1))