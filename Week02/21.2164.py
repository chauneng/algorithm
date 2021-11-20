from sys import stdin
from collections import deque

deck = deque() 

for i in range(1, int(stdin.readline())+1):
    deck.append(i)

while len(deck)>1:
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])