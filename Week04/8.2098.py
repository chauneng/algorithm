from sys import stdin

cities = int(stdin.readline())

arr = [list(map(int, stdin.readline().split())) for _ in range(cities)]

print(arr)