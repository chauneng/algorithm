from sys import stdin

N, M = map(int, stdin.readline().split())
graph = [[] * (N+1) for _ in range(N+1)]

for __ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

parents = list(range(N+1))

def find_parents(num: int) -> int:
    if num == parents[num]:
        return num

    parents[num] = find_parents(parents[num])
    return parents[num]

def union(a: int, b: int):
    pa = find_parents(a)
    pb = find_parents(b)
    
    if pa == pb:
        return

    if pa < pb:
        parents[b] = a
    else:
        parents[a] = b

for i in range(1, len(graph)):
    for j in graph[i]:
        union(j, i)

print(len(set(parents))-1)