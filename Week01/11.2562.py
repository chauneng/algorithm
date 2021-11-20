import sys

num_list = []

for i in range(9):
    num_list.append(int(sys.stdin.readline()))
    
print(max(num_list))
print(num_list.index(max(num_list))+1)

# l = [0, 0]
# i = 0

# while i < 9 :
#     x = int(sys.stdin.readline())
#     i += 1 
#     l[0] = l[0]+1
#     if l[1] < x :
#         l[1] = x
#         l[0] = i
# print(l[1])
# print(l[0])