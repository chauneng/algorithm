from sys import stdin

line = list(stdin.readline().rstrip('\n'))

# print(line)



def check(list_: list):

    smallPointer = 0
    bigPointer = 0
    lastchr = ''
    point = 0
    stack = 0

    for i in range(len(list_)):
        bracket = list_[i]
        
        if bracket == '(':
            smallPointer += 1
            stack = point
        
        elif bracket == ')':
            smallPointer -= 1
            if smallPointer < 0:
                return 0
            else:
                if lastchr == '[':
                    return 0
                elif lastchr == '(':
                    point += 2
                elif lastchr == ')':
                    point *= 2


    lastchr = bracket

print(check(line))