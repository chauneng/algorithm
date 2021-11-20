from sys import stdin
from collections import deque

n = int(stdin.readline())
deck = deque()
    
for _ in range(n):
    instruction = stdin.readline().split()
    if instruction[0] == 'push':
        deck.append(instruction[1])
    elif instruction[0] == 'pop':
        if len(deck):
            print(deck.popleft())
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(deck))
    elif instruction[0] == 'empty':
        if len(deck):
            print(0)
        else:
            print(1)
    elif instruction[0] == 'front':
        if len(deck):
            print(deck[0])
        else:
            print(-1)

    elif instruction[0] == 'back':
        if len(deck):
            print(deck[-1])
        else:
            print(-1)
