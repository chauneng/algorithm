import sys
sys.setrecursionlimit(10**6)

dic = {}
for i in range(int(sys.stdin.readline())):
    dic[i+1] = set()

indoor = [0]
indoor.extend(map(int, sys.stdin.readline().rstrip('\n')))
visited = [0]*(len(dic)+1)

cnt = 0

def dfs(num: int):
    visited[num] = 1
    global n
    for i in dic[num]:

        if not visited[i]:
            if indoor[i]:
                n += 1
            else:
                dfs(i)

for _ in range(len(dic)-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

for j in range(1, len(dic)+1):
    n = 0
    if not indoor[j]:
        if not visited[j]:
            dfs(j)
            cnt += n*(n-1)
    else:
        for k in dic[j]:
            if indoor[k]:
                cnt += 1

print(cnt)
