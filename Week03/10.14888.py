from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
add, sub, mul, div = map(int, stdin.readline().split())

minimum, maximum = float('INF'), -float('INF')

def dfs(depth, res, add, sub, mul, div):
    global minimum, maximum

    if depth == n:
        maximum = max(res, maximum)
        minimum = min(res, minimum)
        return
    
    else:
        if add:
            dfs(depth+1, res+a[depth], add-1, sub, mul, div)
        if sub:
            dfs(depth+1, res-a[depth], add, sub-1, mul, div)
        if mul:
            dfs(depth+1, res*a[depth], add, sub, mul-1, div)
        if div:
            dfs(depth+1, int(res/a[depth]), add, sub, mul, div-1)

dfs(1, a[0], add, sub, mul, div)
print(maximum, minimum, sep='\n')