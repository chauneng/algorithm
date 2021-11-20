from sys import stdin

N = int(stdin.readline())


flag_a = [False] * N
flag_b = [False] * (2*N-1)
flag_c = [False] * (2*N-1) 

count = 0
def set(i: int) -> None:
    global count
    for j in range(N):
        if (    not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j+(N-1)]):

            if i == (N-1):
                count += 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = False



if __name__ == '__main__':
    set(0)
    print(count)