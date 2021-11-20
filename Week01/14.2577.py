import sys

num = 1
for _ in range(3) :
    num = num * int(sys.stdin.readline())
num = str(num)
c = [0]*10
for i in num :
    c[int(i)] += 1
for a in range(10):
    print(c[a], end='\n')
print()
 