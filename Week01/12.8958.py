import sys

c = int(sys.stdin.readline())

for _ in range(c):
    a = sys.stdin.readline()
    stack = 0
    total = 0
    for i in a:
        if i == 'O' :
            stack += 1
            total += stack
        else:
            stack = 0
    print (total)
