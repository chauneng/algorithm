from collections import defaultdict
from sys import stdin
import heapq

N = int(stdin.readline())
M = int(stdin.readline())

routes = defaultdict(list)
totalFare = {i: float('inf') for i in range(1, N+1)}

for _ in range(M):
    departure, arrive, fare = map(int, stdin.readline().split())
    routes[departure].append((arrive, fare))

start, end = map(int, stdin.readline().split())

def dijkstra(start):

    queue = []
    heapq.heappush(queue, (start, 0))

    while queue:
        currentPosition, fare = heapq.heappop(queue)

        if totalFare[currentPosition] < fare:
            continue

        for node in routes[currentPosition]:
            newFare = fare + node[1]
            if totalFare[node[0]] > newFare:
                totalFare[node[0]] = newFare
                heapq.heappush(queue, (node[0], newFare))

dijkstra(start)
print(totalFare[end])