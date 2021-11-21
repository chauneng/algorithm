from sys import stdin

dic = {}

for i in range(int(stdin.readline())):
    dic[i+1] = set()

for j in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

parents = list(range(len(dic)+1))

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

for i in range(1, len(dic)):
    for j in dic[i]:
        union(j, i)

# print(parents)
print(parents.count(1)-1)