import sys

n = int(sys.stdin.readline())
dp = 3
i = 0

while dp < n:
    i += 1
    dp = (dp * 2) + 3 + i

def moo(number: int):
    global n
    n -= int((dp - number - 3)/2)
    if not number:
        n -= 1

        if n == 1 or n==5:
            print('m')
            return
        else:
            print('o')
            return

    if n <= dp - int(((dp - number - 3)/2)):
        if n == 1:
            print('m')

            return
        else:
            print('o')
            return
    else:
        moo(number-1)

if i == 0:
    if n == 1:
        print('m')
    else:
        print('o')
else:
    moo(i)



import sys
n = int(sys.stdin.readline())
arr = 'moo'
for i in range(1, n):
  temp = arr
  arr = temp + 'm'
  if(len(arr) >= n):
    print(arr[n-1])
    break
  elif len(arr) + i+2 >= n:
    print('o')
    break
  arr = temp + 'm' + 'o'*(i+2)+ temp
  if(len(arr) >= n):
    print(arr[n-1])
    break