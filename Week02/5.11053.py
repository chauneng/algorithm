from sys import stdin

a = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
table = []

for i in range(a):
    pl = 0
    pr = len(table)-1
    while pl <= pr:
        pc = (pl+pr)//2
        if table[pc] < li[i]:   
            pl = pc + 1
        else:
            pr = pc - 1
    if pl >= len(table):
        table.append(li[i])
    else:
        table[pl] = li[i]

print(len(table))