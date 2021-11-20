import sys, heapq

V, E = map(int, sys.stdin.readline().split())
edge = []

for _ in range(E):
    a, b, value = map(int, sys.stdin.readline().split())
    # edge.append((value, a, b))
    heapq.heappush(edge, (value, a, b))

# edge.sort(key = lambda x : x[0])
parents = list(range(V+1))

def find_parents(node: int) -> int:
    if node == parents[node]:
        return node

    parents[node] = find_parents(parents[node])
    return parents[node]

def union(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a > b:
        parents[a] = b

    else:
        parents[b] = a

ans = 0

while edge:
# for value, start, end in edge:

    value, start, end = heapq.heappop(edge)

    if find_parents(start) != find_parents(end):
        union(start, end)
        ans += value

print(ans)