from sys import stdin

n, needs = list(map(int, stdin.readline().split()))
height = list(map(int, stdin.readline().split()))
height.append(0)
height.sort()

def micro(min_, max_):
    pl = height[min_]
    pr = height[max_]

    while True:
        pc = (pl+pr)//2
        iTree = sum(height[max_:])-(len(height[max_:])*pc)

        if iTree == needs:
            print(pc)
            return
        
        elif iTree > needs:
            pl = pc + 1
        
        else:
            pr = pc - 1
        
        if pl > pr:
            print(pr)
            return

def macro():

    pl = 0
    pr = len(height)-1

    while True:
        
        pc = (pl+pr)//2
        aTree = sum(height[pc:])-(height[pc]*len(height[pc:]))
        if aTree == needs:
            print(height[pc])
            return
        
        elif aTree > needs:
            pl = pc + 1
        
        else:
            pr = pc - 1
        
        if pl > pr:
            micro(pr,pl)
            return

macro()