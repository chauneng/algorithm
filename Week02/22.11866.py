from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
circle = deque()

print('<', end='')

for i in range(1, n+1):
    circle.append(i)

while len(circle) > 1:
    circle.rotate(-k)
    print(circle.pop(), end=', ')

print(f'{circle[0]}>')
