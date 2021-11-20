from sys import stdin
from typing import get_origin

case = list(map(int, stdin.readline().split()))
size = case[0]
coord = [case[1], case[2]]
li = []

def listing(i : int) :
  if i <= size:
    for j in range((2**i), (2**i)+1):
      for k in range((2**i)-1, (2**i)+1):
        order = [j, k]
        print(order)
        li.append(order)
        listing(i+1)
  else:
    return

if size == 1:
  print('0')
else:
  listing(0)
  # print(li.index(coord))

print(li)