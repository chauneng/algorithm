from sys import stdin

n = int(stdin.readline())
nFactor = list(map(int, stdin.readline().split()))
nFactor.sort()
m = int(stdin.readline())
mFactor = list(map(int, stdin.readline().split()))


for i in mFactor:
    
    pl = 0
    pr = n-1

    while True:
        pc = (pl+pr)//2
        
        if nFactor[pc] == i:
            print(1)
            break
        
        elif nFactor[pc] < i:
            pl = pc + 1
        
        else:
            pr = pc - 1
        
        if pl > pr:
            print(0)
            break