from sys import stdin

firstline = list(map(int, stdin.readline().split()))

m = sorted(list(map(int, stdin.readline().split())))
n = []

for _  in range(firstline[1]):
    n.append(tuple(map(int, stdin.readline().split())))

cnt = 0

for i in n:

    if i[1] <= firstline[2]:
        nOnXMin = i[0] + (i[1] - firstline[2])
        nOnXMax = i[0] - (i[1] - firstline[2])
        pl = 0
        pr = len(m)-1

        while pl <= pr:
            pc = (pl + pr) // 2
            if nOnXMin <= m[pc] <= nOnXMax:
                cnt += 1
                break
            elif nOnXMax < m[pc]:
                pr = pc - 1
            elif m[pc] < nOnXMin:
                pl = pc + 1

print(cnt)