import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

for i in range(n) :
    if l[i] <  x :
        print(l[i], end=" ")
