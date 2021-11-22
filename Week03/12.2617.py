import sys

N, M = map(int, sys.stdin.readline().split())

greater, lesser = {}, {}
ans = 0

for i in range(N):
    greater[i+1] = set()
    lesser[i+1] = set()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    greater[b].add(a)
    lesser[a].add(b)

def dfs(listing: set, num: int):
    for i in list(listing[num]):
        for j in listing[i]:
            if j is None:
                return
            else:
                dfs(listing, j)
                listing[num].add(j)

for i in greater:
    dfs(greater, i)
    if len(greater[i]) >= int((N+1)/2):
        ans += 1
for j in lesser:
    dfs(lesser, j)
    if len(lesser[j]) >= int((N+1)/2):
        ans += 1
        
print(ans)
