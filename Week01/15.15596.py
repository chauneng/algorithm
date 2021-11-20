from sys import stdin

a = list(map(int, stdin.readline().split()))

def solve(a):

    ans = 0
    
    for i in a:
        ans += i
    
    return ans
