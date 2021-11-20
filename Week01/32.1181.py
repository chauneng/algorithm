from sys import stdin
rpt = int(stdin.readline())
li = []

for _ in range(rpt) :
     li.append(input())


listToSet = set(li)
sortedSet = sorted(listToSet)
last = sorted(sortedSet, key=len)

for i in range(len(last)):
     print(last[i])
