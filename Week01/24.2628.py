import sys

paper = list(map(int, sys.stdin.readline().split()))
cut = int(sys.stdin.readline())
rPoint = [0, paper[0]]
cPoint = [0, paper[1]]

for i in range(cut) :
    coord = list(map(int, sys.stdin.readline().split()))
    isRow = coord[0]
    value = coord[1]

    if isRow :
        rPoint.append(value)
    else :
        cPoint.append(value)

rPoint.sort()
cPoint.sort()
width = []
hight = []
areaSize = []

for i in range(1, len(rPoint)) :
    width.append(rPoint[i] - rPoint[i-1])
    for j in range(1, len(cPoint)) :
        hight.append(cPoint[j] - cPoint[j-1])
        areaSize.append(width[i-1]*hight[j-1])
        
print(max(areaSize))