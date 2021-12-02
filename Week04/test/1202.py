from sys import stdin

N, K = map(int, stdin.readline().split())
jewelies = [list(map(int, stdin.readline().split())) for _ in range(N)]
bags = [int(stdin.readline()) for _ in range(K)]
bags.sort()

dp = []