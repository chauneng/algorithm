import sys
sys.setrecursionlimit(10**6)

dic = {}
for i in range(int(sys.stdin.readline())):
    dic[i+1] = set()

indoor = [0]
indoor.extend(map(int, sys.stdin.readline().rstrip('\n')))

cnt = 0

def dfs(num: int):
    visited[num] = 1
    global cnt
    for i in dic[num]:

        if not visited[i]:
            if indoor[i]:
                cnt += 1
            else:
                dfs(i)
        

for _ in range(len(dic)-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

for j in range(1, len(dic)+1):

    visited = [0]*(len(dic)+1)

    if indoor[j]:
        dfs(j)

print(cnt)

# print(list(indoor))
# print(dic)