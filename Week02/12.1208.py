import sys

n = int(sys.stdin.readline())
stack = [0]*n
ptr = 0

def push(i: str):

    global ptr
    global stack

    stack[ptr] = i
    ptr += 1

def pop():
    global ptr

    if ptr == 0:
        return -1
    else:
        ptr-=1
        return stack[ptr]


def size():
    return ptr

def empty():
    if ptr == 0:
        return 1
    else:
        return 0

def top():

    global stack

    if ptr == 0:
        return -1
    else:
        return stack[ptr-1]

for _ in range(n):

    instruction = sys.stdin.readline().split()

    if instruction[0] == 'push':
        push(instruction[1])
    elif instruction[0] == 'size':
        print(size())
    elif instruction[0] == 'pop':
        print(pop())
    elif instruction[0] == 'empty':
        print(empty())
    elif instruction[0] == 'top':
        print(top())