import sys

num = int(sys.stdin.readline())
ans = 1
if num :
    for i in range(1, num+1) :
        ans = ans * i    
print(ans)
