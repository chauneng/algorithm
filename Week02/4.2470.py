from sys import stdin

n = int(stdin.readline())
arr = sorted(map(int, stdin.readline().split()))

start, end = 0 , n-1
leastPh = abs(arr[start]+arr[end])
ans = [arr[start], arr[end]]

while start < end:
    tmp = arr[start]+arr[end]
    if abs(tmp) < leastPh:
        leastPh = abs(arr[start]+arr[end])
        ans = arr[start], arr[end]

    left = arr[start+1] + arr[end]
    right = arr[start] + arr[end-1]

    if abs(left) < abs(right):
        start += 1

    else:
        end -= 1
    
print(' '.join(map(str, sorted(ans))))