from sys import stdin

dic = {}

for i in range(int(stdin.readline())):
    dic[i+1] = set()

for j in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

visited = []

def dfs(start: int, dic: dict):
    for k in dic[start]:
        if k not in visited:
            visited.append(k)
            dfs(k, dic)

# print(parents)
dfs(1, dic)
print(len(visited)-1)