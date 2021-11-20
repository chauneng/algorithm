from sys import stdin

n = int(stdin.readline())
originalPaper = [list(map(int, stdin.readline().split())) for _ in range(n)]
blue = 0
white = 0

def cut(length: int, paper: list):
    first, second = [], []
    for j in paper:
        first.append(j[:length])
        second.append(j[length:])

    checker(length, first)
    checker(length, second)
    # print(first)
    # print(second)

def checker(pLength, paper):
    global white
    global blue
    wholePaper = 0
    for i in paper:
        wholePaper += sum(i)

    if wholePaper == 0:
        white += 1
        # print('white: ', white)
    
    elif wholePaper == pLength ** 2 :
        blue += 1
        # print('blue: ', blue)
    else:
        cut(int(pLength/2), paper[:int(pLength/2)])
        # print(int(pLength/2), paper[:int(pLength/2)])
        cut(int(pLength/2), paper[int(pLength/2):])
        # print(int(pLength/2), paper[int(pLength/2):])

checker(n, originalPaper)
print(white, blue, sep='\n')