from itertools import permutations

p = list(input('p').split())
h = list(input('h').split())

strikes = 0
rest = []

for i in range(3):
    if p[i] == h[i]:
        strikes += 1
    else:
        rest.append(p[i])
        rest.append(h[i])

balls = (len(rest)- len(set(rest)))
print('strikes:', strikes)
print('balls', balls)
print('hStrike', h[1])

# pOptions = permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)
