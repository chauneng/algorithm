from sys import stdin

n = int(stdin.readline())
fluid = sorted(map(int, stdin.readline().split()))
lptr, rptr = 0, n - 1
mostNutral = [lptr, rptr]

def checker(base):

    global mostNutral
    pl = base + 1
    pr = n - 1

    while True:

        pc = (pl+pr)//2
        solution = fluid[base]+fluid[pc]
        
        if solution == 0:
            mostNutral.clear()
            mostNutral.append(fluid[base])
            mostNutral.append(fluid[pc])
            return
        
        elif solution < 0:
            pl = pc + 1
        else:
            pr = pc - 1

        if pl > pr:
            if abs(solution) < abs(sum(mostNutral)):
                mostNutral.clear()
                mostNutral.append(fluid[base])
                mostNutral.append(fluid[pc])
            return

for i in range(n-1):
    if sum(mostNutral):
        checker(i)
    else:
        break

print(" ".join(map(str, sorted(mostNutral))))