import sys

t = int(input())
i = 0

while i < t :
    i += 1
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)