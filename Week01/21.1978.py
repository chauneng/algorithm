from sys import stdin

numRange = 1000
sieve = [True] * numRange
for i in range(2, int(numRange**0.5)) :
    if sieve[i] == True :
        for j in range(i+i, numRange, i) :
            sieve[j] = False
primeNumbers = []
for i in range(2, numRange) :
    if sieve[i] == True :
        primeNumbers.append(i)

case = int(stdin.readline())

num = list(map(int, stdin.readline().split()))

ans = list(set(primeNumbers).intersection(num))

print(len(ans))