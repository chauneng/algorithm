from sys import stdin

a, b, c = map(int, stdin.readline().split())

def f(x, y):
    if y ==1:
        return x % c

    tmp = f(x, y//2)

    if y % 2:
        return tmp * tmp * x % c
    else:
        return tmp * tmp % c
    
print(f(a, b))