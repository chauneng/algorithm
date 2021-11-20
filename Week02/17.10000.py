from sys import stdin

n = int(stdin.readline())
xr = [list(map(int, stdin.readline().split())) for _ in range(n)]

dots = []

for i in xr:
    dots.append((0, i[0]-i[1]))
    dots.append((1, i[0]+i[1]))

dots.sort(reverse=True)
dots.sort(key= lambda x:x[1])

circle_stack = []
cnt = 1
lastLeft = (-1, 0)
lastRight = (-1, 0)
lastLength = 0
strip = [0, 0, 0]

for j in range(len(dots)):
    if not dots[j][0]:
        circle_stack.append(dots[j])
    else:
        right = dots[j]
        left = circle_stack.pop(-1)
        length = right[1] - left[1]

        if left == lastLeft:
            if length == strip[2]:
                strip = [left, right, length]
                cnt += 2
            else:
                lastLength = length
                cnt += 1

        elif (1, left[1]) == lastRight:
            lastLength += length
            strip = (lastLeft, right, lastLength)
            cnt += 1
        
        else:
            lastLength = length
            strip = (left, right, length)
            cnt += 1
        
        lastLeft = left
        lastRight = right
        strip = (left, right, length)

print(cnt)