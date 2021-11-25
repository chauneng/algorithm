#플로이드 와샬?

from sys import stdin

N, M = map(int, stdin.readline())

bridges = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, stdin.readline().split())
    bridges[a][b] = w
    bridges[b][a] = w