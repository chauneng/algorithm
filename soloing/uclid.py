def gdc(a, b):
    if a%b == 0:
        return b
    else:
        return gdc(b, a%b)

print(gdc(192, 162))