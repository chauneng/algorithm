import sys

n = int(sys.stdin.readline())
li = [0]*n
ptr = 0

def num(i: int):
    
    global ptr
    global li
    
    li[ptr] = i
    ptr += 1


def zero():
    
    global ptr
    global li
    ptr -= 1
    li[ptr] = 0

for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        zero()
    else:
        num(m)

print(sum(li))