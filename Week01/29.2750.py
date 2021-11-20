from sys import stdin
rpt = int(stdin.readline())
li = []
for _ in range(rpt):
    li.append(int(stdin.readline()))

li.sort()

for i in range(rpt):
    print(li[i])