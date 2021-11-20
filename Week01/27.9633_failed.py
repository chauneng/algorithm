from sys import stdin

num = int(stdin.readline())
cnt = 0
pos = [0] * num # 각 열에서 퀸의 위치
hrflag = [False] * num #각 행에 퀸을 배치했는지 체크
pdflag = [False] * ((num*2)-1) # /방향으로 퀸을 배치했는지 체크
mdflag = [False] * ((num*2)-1) #\방향으로 퀸을 배치했는지 체크

def setQ(i: int) -> None :
  global cnt
  for j in range(num-1, -1, -1):
    print(i-1, j)
    if (not hrflag[j]
    and not pdflag[i+j-1]
    and not mdflag[i-j+(2*num)-2]):  
      pos[i-1] = j
      if i == 0:
        cnt += 1
      else :
        hrflag[j] = pdflag[i+j-1] = mdflag[i-j+(2*num)-2] = True
        setQ(i - 1)
        hrflag[j] = pdflag[i+j-1] = mdflag[i-j+(2*num)-2] = False

setQ(num)

print(cnt)
