import sys

paper = list(map(int, sys.stdin.readline().split()))
# print(paper)
cut = int(sys.stdin.readline())
# print(cut)
for i in range(cut) :
    coord = list(map(int, sys.stdin.readline().split()))
    value = coord[1]
    horz = paper[0]
    vert = paper[1]
    # print(coord[1])
    if coord[0] :
        a = [0, 0]
        a[0] = horz - value 
        a[1] = value - horz
        paper[0] = max(a)
    
    else :
        b = [0, 0]
        b[0] = vert - value
        b[1] = value - vert
        paper[1] = max(b)

    print(paper)
