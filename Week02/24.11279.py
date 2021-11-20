import heapq, sys

n = int(sys.stdin.readline())
mHeap = []

def f(num: int):
    if num:
        heapq.heappush(mHeap, (-num, num))
    else:
        if mHeap:
            print(heapq.heappop(mHeap)[1])
        else:
            print(0)

for _ in range(n):
    f(int(sys.stdin.readline()))