from sys import stdin

nOfDisk = int(stdin.readline())

cnt = 0
mHistory = []

def output():
    print(cnt)
    if cnt > 20 :
        return
    else:
        for i in range(cnt):
            history = mHistory[i]
            print (history[0], history[1], sep=' ')



def move(no: int, x: int, y: int) -> None:

    global cnt
    global mHistory

    if no > 1 :
        move (no-1, x, 6 - x - y)
    
    cnt += 1
    moves = [x, y]
    mHistory.append(moves)
    # print(f'{cnt}번째 움직임: 원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

    if no > 1 :
        move(no-1, 6 - x - y, y)

move(nOfDisk, 1, 3)
output()