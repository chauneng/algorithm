import sys, heapq

n = int(sys.stdin.readline())
ho =[]
route = []
for _ in range(n):
    ho.append(tuple(map(int, sys.stdin.readline().split())))
# print(commute)
rail = int(sys.stdin.readline())

for i in ho:
    if abs(i[0]-i[1]) <= rail:
        i = sorted(i)
        route.append(i)

route.sort(key=lambda x:x[1])
# print(route)
heap = []
max_route = 0

for r in route:
    # print(r)
    if not heap:
        heapq.heappush(heap, r)
    else:
        while heap[0][0] < r[1]-rail:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, r)
    max_route = max(len(heap), max_route)

print(max_route)