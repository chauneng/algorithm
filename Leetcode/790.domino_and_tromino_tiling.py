n = 30
def numTilings(n):
    if n < 3:
        return n

    dp_r, dp_p = [0]*(n+1), [0]*(n+1)
    for i in range(3):
        dp_r[i]=i
        dp_p[i]=i
    mod = int((1e9)+7)
    for i in range(3, n+1):
        dp_r[i] = (dp_r[i-1]+dp_r[i-2]+2*(dp_p[i-2])) % mod
        dp_p[i] = (dp_r[i-1]+dp_p[i-1]) % mod
    return dp_r[n]

print(numTilings(n))