from itertools import combinations
from sys import stdin


heights = []
for i in range(9):
    heights.append(int(stdin.readline()))

for i in combinations(heights,7):
    if sum(i) == 100 : 
        for j in sorted(i):
            print(j)
        break