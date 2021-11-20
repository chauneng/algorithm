from sys import stdin
rpt = int(stdin.readline())
li = [0] * 10001

for _ in range(rpt) :
     li[int(stdin.readline())] += 1

for i in range(10001):
     if li[i]:
          for j in range(li[i]):
               print(i)