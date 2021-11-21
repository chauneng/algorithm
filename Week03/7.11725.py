import sys

sys.setrecursionlimit(10**7)

dic = {}

for i in range(int(sys.stdin.readline())):
    dic[i+1] = set()

for _ in range(len(dic)-1):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

parents = [0] * (int(len(dic)+1))

def find_child(num: int):
    for i in dic[num]:
        if parents[i] == 0:
            parents[i] = num
            find_child(i)

find_child(1)

for j in range(2, len(parents)):
    print(parents[j])