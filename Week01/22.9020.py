import sys

case = int(sys.stdin.readline())

numRange = 10000
sieve = [True] * numRange
for i in range(2, int(numRange**0.5)) :
    if sieve[i] == True :
        for j in range(i+i, numRange, i) :
            sieve[j] = False

for j in range(case) :
    num = int(sys.stdin.readline())
    for k in range((num//2), 1, -1) :
        if sieve[k] and sieve[num-k]:
            print (k, num-k)
            break
   