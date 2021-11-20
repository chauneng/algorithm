from sys import stdin

n = int(stdin.readline())
ptr = 0

def checker(input_:str):
    global ptr
    if input_ == ')':
        ptr -= 1
    elif input_ == '(':
        ptr += 1
    
    if ptr == -1:
        return False

for _ in range(n):
    line = stdin.readline()
    for i in line:
        if checker(i) == False:
            break
    if ptr == 0:
        print('YES')
        ptr = 0
    else:
        print('NO')
        ptr = 0