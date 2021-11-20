from sys import stdin

a = stdin.readline().split()

first = a[0]
second = a[1]

if first[::-1] < second[::-1] :
    print(second[::-1])
else :
    print(first[::-1])