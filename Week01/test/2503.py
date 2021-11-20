from sys import stdin
from itertools import permutations
from typing import MutableSequence

pOptions = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

def f(h: MutableSequence, s: int, b: int):
    global pOptions
    
    for i in reversed(pOptions):
        strikes = 0
        balls = 0
        rest = []
        for j in range(3):
            if i[j] == h[j]:
                strikes += 1
            else:
                rest.append(i[j])
                rest.append(h[j])
        balls = len(rest) - len(set(rest))
        if [s, b] != [strikes,balls]:
            pOptions.remove(i)
    return
    

def check(i: int):

    if i == 0:
        return
    else:
        hint = stdin.readline().split()
        num = []
        num.append(hint[0][0])
        num.append(hint[0][1]) 
        num.append(hint[0][2])
        strike = int(hint[1])
        ball = int(hint[2])
        f(num, strike, ball)
        check(i-1)

check(int(stdin.readline()))
print(len(pOptions))