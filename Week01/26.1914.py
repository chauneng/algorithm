from sys import stdin

def hanoi(diskN, a, b, c):
    if diskN == 1 :
        print(a, c, sep = " ")
    else:
        hanoi(diskN-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(diskN-1, b, a, c)

diskN = int(stdin.readline())
print(2**diskN-1)
if(diskN <= 20):
    hanoi(diskN, 1, 2, 3)