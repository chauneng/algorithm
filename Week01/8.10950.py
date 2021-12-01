from sys import stdin
N = int(stdin.readline())
for i in range(N):
    a, b = map(int, stdin.readline().split())
    print(a+b)