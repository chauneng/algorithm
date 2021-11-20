# import heapq, sys, copy, math

# n = int(sys.stdin.readline())
# heap = []

# def middle(num: int):
#     tmpHeap = copy.deepcopy(heap)
#     for _ in range(math.ceil(num/2)):
#         midNum = heapq.heappop(tmpHeap)
#     return midNum


# for i in range(n):
#     heapq.heappush(heap, int(sys.stdin.readline()))
#     print(middle(i+1))

import heapq, sys

n = int(sys.stdin.readline())
minHeap, maxHeap= [], []

for i in range(n):
    num = int(sys.stdin.readline())
    if len(maxHeap) == len(minHeap):
        heapq.heappush(maxHeap, (-num, num))
    else:
        heapq.heappush(minHeap, (num, num))
    
    if minHeap and maxHeap[0][1] > minHeap[0][1]:
        maxOfMinHeap = heapq.heappop(minHeap)[1]
        minOfMaxHeap = heapq.heappop(maxHeap)[1]  
        heapq.heappush(minHeap, (minOfMaxHeap, minOfMaxHeap))
        heapq.heappush(maxHeap, (-maxOfMinHeap, maxOfMinHeap))

    print(maxHeap[0][1], end='\n')
print()