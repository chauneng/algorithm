from sys import stdin

# 시간초과
# n = int(stdin.readline())
# towers = [100000001]
# towers.extend(list(map(int, stdin.readline().split())))

# def lazer(height: int, indexNum: int) -> int :

#     for i in range(indexNum-1, -1, -1):
#         if height <= towers[i]:
#             print(i, end=' ')
#             return
#         elif indexNum == 1:
#             return

# for i in reversed(towers):
#     lazer(i, n)
#     n -= 1

n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stack = []
ptr = [0] * n

for i in range(n):
    t = towers[i]
    while stack and towers[stack[-1]] < t:
        stack.pop()
    if stack:
        ptr[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, ptr))))