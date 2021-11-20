from sys import stdin

caseNum = int(stdin.readline())

for _ in range(caseNum):
    case = list(stdin.readline().split())
    rpt = int(case[0])
    for i in case[1] :
        print(i*rpt, end='')
    print()