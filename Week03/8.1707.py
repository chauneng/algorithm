import sys
sys.setrecursionlimit(10**6)

def dfs(v, group):
    visited[v] = group
    for k in dic[v]:
        if visited[k] == 0:
            if not dfs(k, -group):
                return False
        elif visited[k] == visited[v]:
            return False
    return True

for _ in range(int(sys.stdin.readline())):
    
    V, E = map(int, sys.stdin.readline().split())
    
    dic = {}
    visited = [0] * (V+1)
    bipatite = True

    for i in range(V):
        dic[i+1] = set()

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        dic[a].add(b)
        dic[b].add(a)
        
    for i in range(1, V+1):
        if visited[i] == 0:
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')
