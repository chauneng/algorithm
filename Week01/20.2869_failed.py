from sys import stdin

q = list(map(int, stdin.readline().split()))

up = q[0]
down = q[1]
height = q[2]
day = 1
position = up

while position < height :
    day += 1
    position += up
    if position >= height :
        break
    position -= down

print(day)