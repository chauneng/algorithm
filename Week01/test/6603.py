from sys import stdin
from typing import MutableSequence
from itertools import combinations

def exinput():
    num = list(map(int, stdin.readline().split()))
    k = num.pop(0)
    if k == 0:
        return
    else:
        lotto(num)
        exinput()

def lotto(m:MutableSequence):
    cmb = list(combinations(m,6))
    for i in cmb:
        for j in i:
            print(j, end=' ')
        print(sep='\n')
    print()

exinput()