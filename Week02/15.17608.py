from sys import stdin

n = int(stdin.readline())
sticks = []

def checker():
    v = 1
    base = sticks[-1]
    for i in reversed(sticks):
        if i > base:
            v += 1
            base = i
    return v

for _ in range(n):
    sticks.append(int(stdin.readline()))

print(checker())