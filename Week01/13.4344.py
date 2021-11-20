import sys, statistics

c = int(sys.stdin.readline())

for _ in range(c) :

    a = list(map(int, sys.stdin.readline().split()))
    m = statistics.mean(a[1:])
    cnt = 0
    for i in a[1:]:
        if i > m :
            cnt += 1
    ratio = cnt/a[0] * 100
    print(f'{ratio:.3f}%')