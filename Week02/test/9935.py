from collections import deque
from sys import stdin

string = list(stdin.readline().rstrip('\n'))
bomb = list(stdin.readline().rstrip('\n'))
stack = []
lastchr = ''

for i in range(len(string)):
    stack.append(string[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

answer = ''.join(stack)

if answer == '':
    print('FRULA')
else:
    print(answer)
