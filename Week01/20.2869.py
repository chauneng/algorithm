import math, sys
up, down, height = map(int, sys.stdin.readline().split())
day = math.ceil((height-up)/(up-down)) + 1
print(day)